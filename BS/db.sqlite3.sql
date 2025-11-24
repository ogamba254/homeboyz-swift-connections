-- Create the database
CREATE DATABASE bus_booking_system;
USE bus_booking_system;

-- 1. Users Table
CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Buses Table
CREATE TABLE buses (
  bus_id INT AUTO_INCREMENT PRIMARY KEY,
  bus_name VARCHAR(100) NOT NULL,
  plate_number VARCHAR(50) UNIQUE NOT NULL,
  capacity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Routes Table
CREATE TABLE routes (
  route_id INT AUTO_INCREMENT PRIMARY KEY,
  origin VARCHAR(100) NOT NULL,
  destination VARCHAR(100) NOT NULL,
  distance_km INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Schedules Table
CREATE TABLE schedules (
  schedule_id INT AUTO_INCREMENT PRIMARY KEY,
  bus_id INT NOT NULL,
  route_id INT NOT NULL,
  departure_time DATETIME NOT NULL,
  arrival_time DATETIME,
  price_per_seat DECIMAL(10,2) DEFAULT 1500,
  FOREIGN KEY (bus_id) REFERENCES buses(bus_id),
  FOREIGN KEY (route_id) REFERENCES routes(route_id)
);

-- 5. Bookings Table
CREATE TABLE bookings (
  booking_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  schedule_id INT NOT NULL,
  seats_selected VARCHAR(100) NOT NULL,
  total_amount DECIMAL(10,2) NOT NULL,
  status ENUM('Confirmed','Completed','Cancelled') DEFAULT 'Confirmed',
  booked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (schedule_id) REFERENCES schedules(schedule_id)
);

-- 6. Payments Table
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT PRIMARY KEY,
  booking_id INT NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('Pending','Successful','Failed') DEFAULT 'Pending',
  FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);
