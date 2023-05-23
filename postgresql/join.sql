select g.name, count(a.artist_id) artist_q from genres g
join artists_genres ag on g.genre_id = ag.genre_id
join artists a on a.artist_id = ag.artist_id
group by g.name;

select count(t.track_id) track_q from tracks t
join albums al on al.album_id = t.album_id
where al.release_year between 2019 and 2020;

select a.name, avg(t.duration) from albums a
join tracks t on a.album_id = t.album_id 
group by a.name;

select a.name from artists a
where a.name not in (
select a.name from artists a
join albums_artists aa on a.artist_id = aa.artist_id
join albums al on al.album_id = aa.album_id 
where release_year = 2020
);

select c.name from collections c
join collections_tracks ct on c.collection_id = ct.collection_id
join tracks t on t.track_id = ct.track_id
join albums al on al.album_id = t.album_id 
join albums_artists aa on al.album_id = aa.album_id
join artists a on a.artist_id = aa.artist_id 
where a.name = 'Kero Kero Bonito';

select distinct al.name from albums al
join albums_artists aa on al.album_id = aa.album_id 
join artists a on a.artist_id = aa.artist_id 
join artists_genres ag on a.artist_id = ag.artist_id 
group by al.name, ag.artist_id
having count(ag.artist_id) > 1;

select t.name from tracks t
left join collections_tracks ct on t.track_id = ct.track_id 
where ct.track_id is null;

select a.name from artists a
join albums_artists aa on a.artist_id = aa.artist_id 
join albums al on al.album_id = aa.album_id 
join tracks t on t.album_id = al.album_id 
where duration = (select min(duration) from tracks);

select al.name, count(t.track_id) track_count from albums al
join tracks t on t.album_id = al.album_id
group by al.name
having count(t.track_id) = (select min(track_count) from 
(select count(track_id) track_count
from tracks 
group by album_id) track_counts);



