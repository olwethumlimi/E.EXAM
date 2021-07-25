-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2021 at 01:15 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `e_exam`
--
CREATE DATABASE IF NOT EXISTS `e_exam` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `e_exam`;

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `module_name` varchar(255) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `year` varchar(255) NOT NULL,
  `semester` varchar(20) NOT NULL,
  `answer` text NOT NULL,
  `choice` text NOT NULL,
  `question` text NOT NULL,
  `tier` varchar(22) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `module_name`, `course_name`, `year`, `semester`, `answer`, `choice`, `question`, `tier`) VALUES
(1, 'development software', 'it', '1', '1', 'true', 'true ; false', 'Is database management system (DBMS) defined as a collection of programs that manages the database structure and controls access to the data stored in the database.', '1'),
(2, 'info', 'it', '1', '1', 'hacker', 'hacker ; database ; systems ; teacher', 'He is a person who illegally gains access to and sometimes tampers with information in a computer system.', '1'),
(3, 'development software', 'it', '1', '1', 'true', 'true ; false', 'data stored in the database.', '2'),
(4, 'development software', 'it', '1', '1', 'true', 'true ; false', 'SELECT DISTINCT  module_name FROM questions', '3'),
(5, 'info', 'it', '1', '1', 'hacker', 'hacker ; teacher', 'with information in a computer system.', '1'),
(6, 'info', 'it', '1', '1', 'teacher', 'hacker ; teacher', ' computer system.', '1'),
(7, 'info', 'it', '1', '1', 'hacker', 'hacker ; database ; systems ; teacher', 'He is a person who illegally gains access to and sometimes tampers with information in a computer system.', '2'),
(8, 'info', 'it', '1', '1', 'hacker', 'hacker ; teacher', 'with information in a computer system.', '2'),
(9, 'info', 'it', '1', '1', 'teacher', 'hacker ; teacher', ' computer system.', '2'),
(10, 'info', 'it', '1', '1', 'hacker', 'hacker ; database ; systems ; teacher', 'He is a person who illegally gains access to and sometimes tampers with information in a computer system.', '3'),
(11, 'info', 'it', '1', '3', 'hacker', 'hacker ; teacher', 'with information in a computer system.', '3'),
(12, 'info', 'it', '1', '1', 'teacher', 'hacker ; teacher', ' computer system.', '3');

-- --------------------------------------------------------

--
-- Table structure for table `results`
--

CREATE TABLE `results` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `module_name` varchar(255) NOT NULL,
  `semester` varchar(255) NOT NULL,
  `year` varchar(255) NOT NULL,
  `mark` int(11) DEFAULT NULL,
  `type` varchar(255) NOT NULL,
  `test_date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `year` varchar(255) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `semester` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `results`
--
ALTER TABLE `results`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `results`
--
ALTER TABLE `results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
