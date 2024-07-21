-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 21, 2024 at 06:49 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cao`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customers_id` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customers_id`, `first_name`, `last_name`, `email`) VALUES
(1, 'yashmeet', 'kour', 'kour@gmail.com'),
(2, 'meet', 'kakani', 'kakani2@gmail.com'),
(3, 'manav', 'kakani', 'manav@gmail.com'),
(4, 'jay', 'kumar', 'kumarjay@gmail.com'),
(5, 'raj', 'chauhan', 'rajchauhan@gmail.com'),
(6, 'krish', 'chauhan', 'kri@gmail.com'),
(7, 'ronak', 'darjii', 'ron@gmail.com'),
(8, 'devang', 'parekh', 'devang@gmail.com'),
(9, 'dharmik', 'patel', 'dharmik@gmail.com'),
(10, 'yagnik', 'sakariya', 'kano@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `totalamount` decimal(20,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `customer_id`, `order_date`, `totalamount`) VALUES
(1, 6, '2022-05-25', 250.00),
(2, 3, '2023-06-28', 300.00),
(3, 1, '2024-08-05', 800.00),
(4, 2, '2024-09-25', 500.00),
(5, 4, '2024-07-01', 300.00),
(6, 5, '2024-07-10', 200.00),
(7, 7, '2024-07-24', 50.00),
(8, 9, '2024-05-22', 500.00),
(9, 10, '2024-03-12', 600.00),
(10, 8, '2024-02-13', 250.00);

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE `order_details` (
  `order_detail_id` int(11) NOT NULL,
  `orders_id` int(11) DEFAULT NULL,
  `products_id` int(11) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_details`
--

INSERT INTO `order_details` (`order_detail_id`, `orders_id`, `products_id`, `quantity`, `price`) VALUES
(1, 1, 1, 2, 100),
(2, 1, 4, 1, 50),
(3, 2, 2, 1, 200),
(4, 2, 4, 1, 50),
(5, 2, 5, 1, 50),
(6, 3, 3, 2, 400),
(7, 4, 4, 2, 50),
(8, 4, 3, 1, 400),
(9, 5, 2, 1, 200),
(10, 5, 1, 1, 100),
(11, 6, 2, 1, 200),
(12, 7, 5, 1, 50),
(13, 8, 6, 1, 500),
(14, 9, 1, 1, 100),
(15, 9, 6, 1, 500),
(16, 10, 5, 1, 50),
(17, 10, 1, 2, 100);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `product_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `product_price`) VALUES
(1, 'Pvp Pipe 25Mm', 100),
(2, 'Pvp Door', 200),
(3, 'Pvc Penel Wall', 400),
(4, 'scroo', 50),
(5, 'scroo nut', 50),
(6, 'bed', 500);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customers_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`order_detail_id`),
  ADD KEY `orders_id` (`orders_id`),
  ADD KEY `products_id` (`products_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customers_id`);

--
-- Constraints for table `order_details`
--
ALTER TABLE `order_details`
  ADD CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`orders_id`) REFERENCES `orders` (`order_id`),
  ADD CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`products_id`) REFERENCES `products` (`product_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
