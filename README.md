# micropython-basicdweet
[![PayPal Donate][paypal_img]][paypal_link]
[![PyPI version][pypi_img]][pypi_link]
[![Downloads][downloads_img]][downloads_link]

  [paypal_img]: https://github.com/jacklinquan/images/blob/master/paypal_donate_badge.svg
  [paypal_link]: https://www.paypal.me/jacklinquan
  [pypi_img]: https://badge.fury.io/py/micropython-basicdweet.svg
  [pypi_link]: https://badge.fury.io/py/micropython-basicdweet
  [downloads_img]: https://pepy.tech/badge/micropython-basicdweet
  [downloads_link]: https://pepy.tech/project/micropython-basicdweet

A python module for very basic APIs of the free dweet service.
Dweet is a simple machine-to-machine (M2M) service from [dweet.io](https://dweet.io).

This module only supports these dweet APIs of the free dweet service:

- `dweet for`
- `get latest dweet for`
- `get dweets for`

This module works under MicroPython and it is tested with MicroPython V1.18.

For a compatible CPython version, please find [Python package basicdweet](https://github.com/jacklinquan/basicdweet).

## Installation
``` Python
>>> import upip
>>> upip.install('micropython-basicdweet')
```
Alternatively just copy basicdweet.py to the MicroPython device.

## Usage
``` python
>>> import basicdweet
>>> basicdweet.dweet_for('YOUR THING', {'YOUR DATA': 'YOUR VALUE'})
{'thing': 'YOUR THING', 'created': '2022-05-27T03:57:41.718Z', 'content': {'YOUR DATA': 'YOUR VALUE'}, 'transaction': 'da3d8f20-9b39-4d9a-aa06-2c1eebe0666f'}
>>> basicdweet.get_latest_dweet_for('YOUR THING')
[{'thing': 'YOUR THING', 'created': '2022-05-27T03:57:41.718Z', 'content': {'YOUR DATA': 'YOUR VALUE'}}]
>>> basicdweet.dweet_for('YOUR THING', {'YOUR DATA': 'YOUR VALUE 2'})
{'thing': 'YOUR THING', 'created': '2022-05-27T03:59:14.297Z', 'content': {'YOUR DATA': 'YOUR VALUE 2'}, 'transaction': 'e851fd9e-14c6-4d2b-847a-d9bf8402db18'}
>>> basicdweet.get_latest_dweet_for('YOUR THING')
[{'thing': 'YOUR THING', 'created': '2022-05-27T03:59:14.297Z', 'content': {'YOUR DATA': 'YOUR VALUE 2'}}]
>>> basicdweet.get_dweets_for('YOUR THING')
[{'thing': 'YOUR THING', 'created': '2022-05-27T03:59:14.297Z', 'content': {'YOUR DATA': 'YOUR VALUE 2'}}, {'thing': 'YOUR THING', 'created': '2022-05-27T03:57:41.718Z', 'content': {'YOUR DATA': 'YOUR VALUE'}}]
```
