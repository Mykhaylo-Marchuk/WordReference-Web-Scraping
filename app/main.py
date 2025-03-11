from dotenv import load_dotenv

from app.services.telegram.bot import main

load_dotenv()

if __name__ == '__main__':
    import asyncio

    asyncio.run(main())