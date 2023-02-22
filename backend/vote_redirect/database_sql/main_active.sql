/*
 Navicat MySQL Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80024 (8.0.24)
 Source Host           : 175.178.12.179:3306
 Source Schema         : vote

 Target Server Type    : MySQL
 Target Server Version : 80024 (8.0.24)
 File Encoding         : 65001

 Date: 22/02/2023 10:35:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for main_active
-- ----------------------------
DROP TABLE IF EXISTS `main_active`;
CREATE TABLE `main_active` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `domain_list` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_active
-- ----------------------------
BEGIN;
INSERT INTO `main_active` (`id`, `domain_list`) VALUES (1, '[]');
INSERT INTO `main_active` (`id`, `domain_list`) VALUES (2, '[]');
INSERT INTO `main_active` (`id`, `domain_list`) VALUES (3, '[]');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
