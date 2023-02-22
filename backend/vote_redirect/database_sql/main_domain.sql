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

 Date: 22/02/2023 10:35:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for main_domain
-- ----------------------------
DROP TABLE IF EXISTS `main_domain`;
CREATE TABLE `main_domain` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `domain` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `status` int NOT NULL,
  `vis_cnt` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_domain
-- ----------------------------
BEGIN;
INSERT INTO `main_domain` (`id`, `domain`, `status`, `vis_cnt`) VALUES (1, 'www.baidu.com', 1, 5);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
