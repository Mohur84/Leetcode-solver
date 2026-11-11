from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        current_date=datetime.strptime(date, "%Y-%m-%d")
        return current_date.timetuple().tm_yday