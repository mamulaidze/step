-- სასტუმროს შეყვანა
-- INSERT INTO hotels (name, city, stars)
-- VALUES
-- ('Tbilisi Palace', 'Tbilisi', 5),
-- ('Batumi Sea Hotel', 'Batumi', 4);

-- select * from hotels;


-- ოთახების დამატება
-- INSERT INTO rooms (hotel_id, room_number, floor, night_price)
-- VALUES
-- (1, '101', 1, 120.00),
-- (1, '102', 1, 150.00),
-- (1, '201', 2, 200.00),
-- (2, '301', 3, 100.00),
-- (2, '302', 3, 130.00),
-- (2, '401', 4, 180.00);

-- select * from rooms 

-- INSERT INTO guests (room_id, first_name, last_name, phone)
-- VALUES
-- (1, 'Giorgi', 'Beridze', '599111111'),
-- (1, 'Nino', 'Beridze', '599222222'),
-- (2, 'Luka', 'Kapanadze', '599333333'),
-- (2, 'Mariam', 'Lomidze', '599444444'),
-- (3, 'Saba', 'Gelashvili', '599555555'),
-- (3, 'Ana', 'Maisuradze', '599666666'),
-- (4, 'Davit', 'Tsiklauri', '599777777'),
-- (4, 'Elene', 'Japaridze', '599888888'),
-- (5, 'Irakli', 'Kiknadze', '599999999'),
-- (5, 'Tamar', 'Abashidze', '598111111'),
-- (6, 'Mate', 'Gogoladze', '598222222'),
-- (6, 'Salome', 'Nozadze', '598333333');

-- select * from guests

-- INSERT INTO services (room_id, service_name, service_price)
-- VALUES
-- (1, 'Breakfast', 25.00),
-- (1, 'Laundry', 15.00),
-- (2, 'Spa', 60.00),
-- (2, 'Room Cleaning', 20.00),
-- (3, 'Dinner', 40.00),
-- (3, 'Airport Transfer', 50.00),
-- (4, 'Breakfast', 20.00),
-- (4, 'Parking', 10.00),
-- (5, 'Laundry', 15.00),
-- (5, 'Mini Bar', 30.00),
-- (6, 'Spa', 55.00),
-- (6, 'Dinner', 35.00);

-- select * from services

-- SELECT rooms.room_number, rooms.floor, rooms.night_price, hotels.name AS hotel_name
-- FROM rooms
-- JOIN hotels ON rooms.hotel_id = hotels.hotel_id;


-- SELECT guests.first_name, guests.last_name, guests.phone,
--        rooms.room_number,
--        hotels.name AS hotel_name
-- FROM guests
-- JOIN rooms ON guests.room_id = rooms.room_id
-- JOIN hotels ON rooms.hotel_id = hotels.hotel_id;


-- SELECT guests.first_name, guests.last_name, rooms.room_number, hotels.name AS hotel_name
-- FROM guests
-- JOIN rooms ON guests.room_id = rooms.room_id
-- JOIN hotels ON rooms.hotel_id = hotels.hotel_id
-- WHERE hotels.name = 'Tbilisi Palace';


-- SELECT hotels.name AS hotel_name, COUNT(rooms.room_id) AS rooms_count
-- FROM hotels
-- LEFT JOIN rooms ON hotels.hotel_id = rooms.hotel_id
-- GROUP BY hotels.name;

-- DELETE FROM rooms
-- WHERE room_id = 1;

-- UPDATE rooms
-- SET night_price = 170.00
-- WHERE room_id = 2;


-- UPDATE guests
-- SET room_id = 3
-- WHERE guest_id = 4;
