select name, release_year from albums
where release_year = 2018

select name, duration from tracks 
order by duration desc
limit 1

select name from tracks 
where duration >= 210

select name from collections
where release_year between 2018 and 2020

select name from artists 
where name not like '% %'

select name from tracks
where name like '%My%'

