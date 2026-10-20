class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map={emp.id: emp for emp in employees}
        def dfs(emp_id):
            employee=employee_map[emp_id]
            total=employee.importance
            for sub_id in employee.subordinates:
                total+=dfs(sub_id)
            return total
        return dfs(id)