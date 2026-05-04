import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get("8008398482:AAGMlJYAQj3NuM0NnrkFx7-PPSPO56YBKvA")
ADMIN_ID = int(os.environ.get("7132963801"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

products = {
    "premium_1m": {"name": "💎 Premium 1 oylik", "price": "45,000 so'm"},
    "premium_1y": {"name": "💎 Premium 1 yillik", "price": "350,000 so'm"},
    "gift_3m": {"name": "🎁 Gift 3 oylik", "price": "185,000 so'm"},
    "gift_6m": {"name": "🎁 Gift 6 oylik", "price": "235,000 so'm"},
    "stars_15": {"name": "⭐ 15 Stars", "price": "5,000 so'm"},
    "stars_25": {"name": "⭐ 25 Stars", "price": "10,000 so'm"},
    "stars_50": {"name": "⭐ 50 Stars", "price": "15,000 so'm"},
    "stars_75": {"name": "⭐ 75 Stars", "price": "22,000 so'm"},
    "stars_100": {"name": "⭐ 100 Stars", "price": "24,000 so'm"},
    "stars_150": {"name": "⭐ 150 Stars", "price": "38,000 so'm"},
    "stars_250": {"name": "⭐ 250 Stars", "price": "65,000 so'm"},
    "stars_350": {"name": "⭐ 350 Stars", "price": "90,000 so'm"},
    "stars_500": {"name": "⭐ 500 Stars", "price": "125,000 so'm"},
    "stars_1000": {"name": "⭐ 1000 Stars", "price": "240,000 so'm"},
}

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 Telegram Premium", callback_data="premium")],
        [InlineKeyboardButton(text="🎁 Premium Sovg'a", callback_data="gift")],
        [InlineKeyboardButton(text="⭐ Telegram Stars", callback_data="stars")],
        [InlineKeyboardButton(text="📞 Aloqa", callback_data="contact")],
    ])
    await message.answer(
        "🔔 Jony Premium xizmatiga xush kelibsiz!\n\n"
        "⭐ Stars, 💎 Premium va 🎁 Sovg'alar!\n\n"
        "Quyidagilardan birini tanlang:",
        reply_markup=keyboard
    )

@dp.callback_query(lambda c: c.data == "premium")
async def premium_menu(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 1 oylik — 45,000 so'm", callback_data="buy_premium_1m")],
        [InlineKeyboardButton(text="💎 1 yillik — 350,000 so'm", callback_data="buy_premium_1y")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")],
    ])
    await callback.message.edit_text(
        "💎 Telegram Premium\n\n"
        "Profilingizga kirib olib berish narxi:",
        reply_markup=keyboard
    )

@dp.callback_query(lambda c: c.data == "gift")
async def gift_menu(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎁 3 oylik — 185,000 so'm", callback_data="buy_gift_3m")],
        [InlineKeyboardButton(text="🎁 6 oylik — 235,000 so'm", callback_data="buy_gift_6m")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")],
    ])
    await callback.message.edit_text(
        "🎁 Premium Sovg'a\n\n"
        "Profilingizga kirmasdan sovg'a qilish:",
        reply_markup=keyboard
    )

@dp.callback_query(lambda c: c.data == "stars")
async def stars_menu(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭐ 15 Stars — 5,000 so'm", callback_data="buy_stars_15")],
        [InlineKeyboardButton(text="⭐ 25 Stars — 10,000 so'm", callback_data="buy_stars_25")],
        [InlineKeyboardButton(text="⭐ 50 Stars — 15,000 so'm", callback_data="buy_stars_50")],
        [InlineKeyboardButton(text="⭐ 75 Stars — 22,000 so'm", callback_data="buy_stars_75")],
        [InlineKeyboardButton(text="⭐ 100 Stars — 24,000 so'm", callback_data="buy_stars_100")],
        [InlineKeyboardButton(text="⭐ 150 Stars — 38,000 so'm", callback_data="buy_stars_150")],
        [InlineKeyboardButton(text="⭐ 250 Stars — 65,000 so'm", callback_data="buy_stars_250")],
        [InlineKeyboardButton(text="⭐ 350 Stars — 90,000 so'm", callback_data="buy_stars_350")],
        [InlineKeyboardButton(text="⭐ 500 Stars — 125,000 so'm", callback_data="buy_stars_500")],
        [InlineKeyboardButton(text="⭐ 1000 Stars — 240,000 so'm", callback_data="buy_stars_1000")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")],
    ])
    await callback.message.edit_text("⭐ Telegram Stars tanlang:", reply_markup=keyboard)

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
        f"💳 To'lov rekvizitlari:\n"
        f"💳 Karta: 9860 1766 1848 4958\n"
        f"📱 Click: +998 94 399 03 53\n\n"
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
    await callback.message.edit_text("⏳ To'lovingiz tekshirilmoqda...\nTez orada admin tasdiqlaydi!")

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
        "Muammo bo'lsa admin bilan bog'laning: @jony_xD"
    )
    await callback.message.edit_text("❌ Rad etildi!")

@dp.callback_query(lambda c: c.data == "contact")
async def contact(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "📞 Aloqa:\n\n"
        "👤 Admin: @jony_xD\n"
        "⏰ Ish vaqti: 9:00 — 22:00\n\n"
        "Savollaringiz bo'lsa murojaat qiling!"
    )

@dp.callback_query(lambda c: c.data == "back")
async def go_back(callback: types.CallbackQuery):
    await start(callback.message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
