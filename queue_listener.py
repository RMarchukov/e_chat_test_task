import asyncio
import aio_pika


async def process_message(message: aio_pika.abc.AbstractIncomingMessage) -> None:
    async with message.process():
        print(message.body)
        await asyncio.sleep(1)


async def main() -> None:
    connection = await aio_pika.connect_robust("amqp://guest:guest@127.0.0.1/")
    queue_name = "0"
    channel = await connection.channel()

    await channel.set_qos(prefetch_count=100)
    queue = await channel.declare_queue(queue_name, auto_delete=True)
    await queue.consume(process_message)

    try:
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as err:
        print(err)
