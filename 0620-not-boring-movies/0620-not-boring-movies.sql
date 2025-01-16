/* Write your T-SQL query statement below */
select * from cinema where not id % 2 = 0 and not description = 'boring' order by rating desc 