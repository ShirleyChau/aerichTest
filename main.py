from settings import TORTOISE_ORM
from tortoise import Tortoise, run_async
from models import Info

async def run():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
    await Info.create(msg="Test1")
    print(*(await Info.all().values()),sep="\n")

if __name__ == "__main__":
    run_async(run())
