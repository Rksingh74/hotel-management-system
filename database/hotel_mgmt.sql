-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 11, 2023 at 09:22 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_mgmt`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `ref` int(200) NOT NULL,
  `Name` varchar(200) NOT NULL,
  `Mother` varchar(200) NOT NULL,
  `Gender` varchar(200) NOT NULL,
  `Postcode` varchar(200) NOT NULL,
  `Mobile` varchar(200) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `Nationality` varchar(200) NOT NULL,
  `Idproof` varchar(200) NOT NULL,
  `Idnumber` varchar(200) NOT NULL,
  `Address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`ref`, `Name`, `Mother`, `Gender`, `Postcode`, `Mobile`, `Email`, `Nationality`, `Idproof`, `Idnumber`, `Address`) VALUES
(2, 'rahul', 'abc', 'Male', '274703', '7487825735', 'rahul288402@gmail.com', 'India', 'AAdhar card', '147852369741', 'ayodhya'),
(5, 'asd', 'oij', 'Male', 'bnm,.', '7894561237', 'rks288402@gmail.com', 'India', 'AAdhar card', '741358', 'hbhbja');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `Floor` varchar(200) NOT NULL,
  `Roomno` varchar(200) NOT NULL,
  `Roomtype` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`Floor`, `Roomno`, `Roomtype`) VALUES
('1', '102', 'Luxury'),
('1', '20', 'Luxury'),
('1', '202', 'Luxury'),
('1', '205', 'Luxury'),
('1', '209', 'Luxury'),
('8', '501', 'Double');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `contact` int(200) NOT NULL,
  `check-in` varchar(200) NOT NULL,
  `check-out` varchar(200) NOT NULL,
  `roomtype` varchar(200) NOT NULL,
  `roomavailable` varchar(200) NOT NULL,
  `meal` varchar(200) NOT NULL,
  `noofdays` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`contact`, `check-in`, `check-out`, `roomtype`, `roomavailable`, `meal`, `noofdays`) VALUES
(2147483647, '15/01/2023', '15/03/2023', 'Luxury', '209', 'Breakfast', '42');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ref`);

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`Roomno`),
  ADD KEY `Floor` (`Floor`,`Roomno`) USING BTREE;

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`roomavailable`);

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `password` (`password`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
