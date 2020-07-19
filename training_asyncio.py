import asyncio


async def manager_solve_fact(fact: int):
    res = await solve_fact(fact)
    print(str(fact) + '! = ' + str(res))


async def solve_fact(fact: int):
    factorial: int = fact
    if factorial > 0:
        if factorial > 1:
            factorial * await solve_fact(factorial - 1)  # Это нужно для замедления работы потока
            await asyncio.sleep(0)
            return factorial * await solve_fact(factorial - 1)
        else:
            return 1
    else:
        return 0


async def main():
    for i in range(5):
        ms = input('Какой факториал нужен?')
        loop.create_task(manager_solve_fact(int(ms)))
        await asyncio.sleep(0)
        print('lol')
    loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
    pending = asyncio.Task.all_tasks(loop=loop)
    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()

