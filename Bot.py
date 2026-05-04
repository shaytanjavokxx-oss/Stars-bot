import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# === O'ZING TO'LDIRASAN ===
TOKEN = "8008398482:AAGMlJYAQj3NuM0NnrkFx7-PPSPO56YBKvA"
ADMIN_ID = 7132963801

bot = Bot(token=TOKEN)
dp = Dispatcher()

products = {
    "stars_50": {"name": "⭐ 50 Stars", "price": "25,000 so'm"},
    "stars_100": {"name": "⭐ 100 Stars", "price": "45,000 so'm"},
    "stars_500": {"name": "⭐ 500 Stars", "price": "200,000 so'm"},
    "premium_1": {"name": "💎 Premium 1 oy", "price": "40,000 so'm"},
    "premium_3": {"name": "💎 Premium 3 oy", "price": "180,000 so'm"},
}

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭐ Stars sotib olish", callback_data="stars")],
        [InlineKeyboardButton(text="💎 Premium sotib olish", callback_data="premium")],
        [InlineKeyboardButton(text="🎁 Sovg'a yuborish", callback_data="gift")],
        [InlineKeyboardButton(text="📞 Aloqa", callback_data="contact")],
    ])
    await message.answer(
        "👋 Xush kelibsiz!\n\n"
        "🌟 Stars, Premium va sovg'alar sotib oling!\n\n"
        "Quyidagilardan birini tanlang:",
        reply_markup=keyboard
    )

@dp.callback_query(lambda c: c.data == "stars")
async def stars_menu(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭐ 50 Stars — 25,000 so'm", callback_data="buy_stars_50")],
        [InlineKeyboardButton(text="⭐ 100 Stars — 45,000 so'm", callback_data="buy_stars_100")],
        [InlineKeyboardButton(text="⭐ 500 Stars — 200,000 so'm", callback_data="buy_stars_500")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")],
    ])
    await callback.message.edit_text("⭐ Stars tanlang:", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data == "premium")
async def premium_menu(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 1 oy — 80,000 so'm", callback_data="buy_premium_1")],
        [InlineKeyboardButton(text="💎 3 oy — 220,000 so'm", callback_data="buy_premium_3")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")],
    ])
    await callback.message.edit_text("💎 Premium tanlang:", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith("buy_"))
async def buy_product(callback: types.CallbackQuery):
    product_key = callback.data.replace("buy_", "")
    product = products.get(product_key)
    if not product:
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ To'lov qildim", callback_data=f"paid_{product_key}")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")],
    ])
    await callback.message.edit_text(
        f"🛒 Siz tanladingiz: {product['name']}\n"
        f"💰 Narx: {product['price']}\n\n"
        f"💳 To'lov:\n"
        f"Click: +998XXXXXXXXX\n"
        f"Karta: 8600 XXXX XXXX XXXX\n\n"
        f"✅ To'lov qilgach tugmani bosing!",
        reply_markup=keyboard
    )

@dp.callback_query(lambda c: c.data.startswith("paid_"))
async def payment_done(callback: types.CallbackQuery):
    product_key = callback.data.replace("paid_", "")
    product = products.get(product_key)
    user = callback.from_user
    await bot.send_message(
        ADMIN_ID,
        f"🔔 Yangi buyurtma!\n\n"
        f"👤 {user.full_name}\n"
        f"🆔 {user.id}\n"
        f"📦 {product['name']}\n"
        f"💰 {product['price']}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"confirm_{user.id}_{product_key}")],
            [InlineKeyboardButton(text="❌ Rad etish", callback_data=f"reject_{user.id}")],
        ])
    )
    await callback.message.edit_text("⏳ To'lovingiz tekshirilmoqda...")

@dp.callback_query(lambda c: c.data.startswith("confirm_"))
async def confirm_order(callback: types.CallbackQuery):
    parts = callback.data.split("_")
    user_id = int(parts[1])
    product_key = parts[2]
    product = products.get(product_key)
    await bot.send_message(user_id,
        f"✅ To'lovingiz tasdiqlandi!\n"
        f"📦 {product['name']} yaqin orada yuboriladi!\n"
        f"Rahmat! 🙏"
    )
    await callback.message.edit_text("✅ Tasdiqlandi!")

@dp.callback_query(lambda c: c.data.startswith("reject_"))
async def reject_order(callback: types.CallbackQuery):
    user_id = int(callback.data.split("_")[1])
    await bot.send_message(user_id,
        "❌ To'lovingiz tasdiqlanmadi.\n"
        "Muammo bo'lsa admin bilan bog'laning!"
    )
    await callback.message.edit_text("❌ Rad etildi!")

@dp.callback_query(lambda c: c.data == "contact")
async def contact(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "📞 Aloqa:\n\n"
        "Admin: @USERNAME\n"
        "Ish vaqti: 9:00 — 22:00"
    )

@dp.callback_query(lambda c: c.data == "back")
async def go_back(callback: types.CallbackQuery):
    await start(callback.message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
