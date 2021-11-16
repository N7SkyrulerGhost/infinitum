import asyncio
import logging
import v2ray

logging.getLogger().setLevel(logging.getLevelName('INFO'))


class FakeAirport(v2ray.Airport):
    async def pull_node_list(self) -> list:
        settings = {
            "servers": [
                {
                    "address": '127.0.0.1',
                    "port": 12345,
                    "method": "chacha20",
                    "password": "qwerty",
                }
            ]
        }
        node = v2ray.Node(tag=f'node@{self.airport_name}', protocol='shadowsocks', settings=settings)
        return [node, ]

async def main():
    v = v2ray.V2Ray(config_path='/etc/v2ray/config.json')
    v.airport_list.append(FakeAirport(airport_name='fake.com', max_devices=1))
    await v.run()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
