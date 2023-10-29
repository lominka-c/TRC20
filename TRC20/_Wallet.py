import requests, datetime as dt

erors = {
	"200": "Операція пройшла успішно",
	
	"401": "Користувач не ініціалізований! Введіть `address` гаманця користувача (TRC20)",
	"402": "Невірно вказаний аргумен `only_to` або `only_from` у метожі `last_transaction. Значення повинно бути True або False`",
	"403": "не може бути одночасно `only_from` i `only_to`",
	"405": "Ви неправильно передали параметр lt(lastTransaction)",
	"406": "Валюта не USDT",
	"407": "Транзакція не вірна, здійснено не поповнення на адрес а вивід!",
	"408": "`lastTransaction` повинно містити 1 транзакцію!",
	"409":"Час транзакції раніше ніж ліміт",
}

version = 0.1

class USER_WALLET():
	def __init__(self, address=0):
		if address == 0: print("Error 401")
		else:
			self.address = address
	def errors(self, code=0):
		if code==0:
			print("Вкажіть код помилки!")
		else:
			print(erors[str(code)])
	def last_transactions(self, limit=1, only_from:bool = False, only_to:bool = False):
		if type(only_from) != bool or type(only_to) != bool: return {"Status": "402"}
		if only_from == True and only_to == True:
			return {
				"Status": "403"
			}
		if only_from == True:
			r = requests.get(f"https://api.trongrid.io/v1/accounts/{self.address}/transactions/trc20", headers = {"accept": "application/json"}, params={"limit": limit, "only_from": "True"})
		elif only_to == True:
			r = requests.get(f"https://api.trongrid.io/v1/accounts/{self.address}/transactions/trc20", headers = {"accept": "application/json"}, params={"limit": limit, "only_to": "True"})
		elif only_from == False and only_to == False:
			r = requests.get(f"https://api.trongrid.io/v1/accounts/{self.address}/transactions/trc20", headers = {"accept": "application/json"}, params={"limit": limit})
		lt = []
		for tr in r.json().get("data", []):
			symbol = tr.get("token_info", {}).get("symbol")
			time = tr.get("block_timestamp")
			frrom = tr.get("from")
			too = tr.get("to")
			value = tr.get("value", "")
			decimals = int(tr.get("token_info", {}).get("decimals", "6"))
			dec = -1 * decimals
			f = float(value[:dec] + "." + value[dec:])
			lt.append({
				"Status": "200",
				"time": (dt.datetime.fromtimestamp(float(time)/1000)),
				"amount": f,
				"nano_amount": value,
				"currency": symbol,
				"from": frrom,
				"to": too,
			})
			
		return lt
	def get_address(self):
		return self.address
	def version(self):
		return version
	def deposit(self, lt:list = 0, time=5):
		if type(lt) != list: return {
							"Status": "405"
						}
		else:
			ll = lt
			lt = lt[0]
			if len(ll) != 1: return {"Status":"408"}
			elif lt.get("currency") == "USDT":
				now = dt.datetime.now()
				n = dt.timedelta(minutes=int(5))
				time = lt.get("time")
				if now-n<=time: 
					amount = lt.get("amount")
					if lt.get("to") == self.address:
						return {
							"Status": "200",
							"amount": amount,
							"currency": lt.get("currency"),
						}
					else:
						return {
							"Status": "407"
						}
				else:
					return {"Status": "409"}
			else:
				return {
							"Status": "406"
				}
