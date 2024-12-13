-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 04, 2024 at 12:41 PM
-- Server version: 10.6.17-MariaDB
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ocms_lizfashion`
--

-- --------------------------------------------------------

--
-- Table structure for table `lib_knit_mc_cause`
--

CREATE TABLE `lib_knit_mc_cause` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `created_by` int(10) UNSIGNED NOT NULL,
  `created_at` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_by` int(10) UNSIGNED DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci ROW_FORMAT=COMPACT;

--
-- Dumping data for table `lib_knit_mc_cause`
--

INSERT INTO `lib_knit_mc_cause` (`id`, `name`, `created_by`, `created_at`, `updated_by`, `updated_at`, `deleted_at`) VALUES
(1, 'Yarn Breakage', 1, '2024-10-31 11:37:11', 1, '2024-10-31 11:38:46', NULL),
(2, 'Roll Cutting', 1, '2024-10-31 11:39:17', NULL, NULL, NULL),
(3, 'Needle Breakage', 1, '2024-10-31 11:39:43', NULL, NULL, NULL),
(4, 'Program Change', 1, '2024-10-31 11:40:03', NULL, NULL, NULL),
(5, 'Power', 1, '2024-10-31 11:40:14', NULL, NULL, NULL),
(6, 'Maintence', 1, '2024-10-31 11:40:23', NULL, NULL, NULL),
(7, 'No Order / No Program', 1, '2024-10-31 11:40:43', NULL, NULL, NULL),
(8, 'No Yarn', 1, '2024-10-31 11:40:57', NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lib_knit_mc_cause`
--
ALTER TABLE `lib_knit_mc_cause`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UK_j6cwks7xecs5jov19ro8ge3qk` (`name`),
  ADD KEY `FKp4m1ja47tfe808hk3rqrwtkdp` (`created_by`),
  ADD KEY `updated_by` (`updated_by`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lib_knit_mc_cause`
--
ALTER TABLE `lib_knit_mc_cause`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
