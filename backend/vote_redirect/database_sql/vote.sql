/*
 Navicat MySQL Data Transfer

 Source Server         : 192.168.0.135_3306
 Source Server Type    : MySQL
 Source Server Version : 80032 (8.0.32)
 Source Host           : 192.168.0.135:3306
 Source Schema         : vote

 Target Server Type    : MySQL
 Target Server Version : 80032 (8.0.32)
 File Encoding         : 65001

 Date: 02/03/2023 11:50:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (25, 'Can add active', 7, 'add_active');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (26, 'Can change active', 7, 'change_active');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (27, 'Can delete active', 7, 'delete_active');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (28, 'Can view active', 7, 'view_active');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (29, 'Can add domain', 8, 'add_domain');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (30, 'Can change domain', 8, 'change_domain');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (31, 'Can delete domain', 8, 'delete_domain');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (32, 'Can view domain', 8, 'view_domain');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (33, 'Can add logs', 9, 'add_logs');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (34, 'Can change logs', 9, 'change_logs');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (35, 'Can delete logs', 9, 'delete_logs');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (36, 'Can view logs', 9, 'view_logs');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (37, 'Can add official account', 10, 'add_officialaccount');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (38, 'Can change official account', 10, 'change_officialaccount');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (39, 'Can delete official account', 10, 'delete_officialaccount');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (40, 'Can view official account', 10, 'view_officialaccount');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (41, 'Can add token', 11, 'add_token');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (42, 'Can change token', 11, 'change_token');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (43, 'Can delete token', 11, 'delete_token');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (44, 'Can view token', 11, 'view_token');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (45, 'Can add user', 12, 'add_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (46, 'Can change user', 12, 'change_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (47, 'Can delete user', 12, 'delete_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (48, 'Can view user', 12, 'view_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (49, 'Can add vote activity', 13, 'add_voteactivity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (50, 'Can change vote activity', 13, 'change_voteactivity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (51, 'Can delete vote activity', 13, 'delete_voteactivity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (52, 'Can view vote activity', 13, 'view_voteactivity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (53, 'Can add vote user', 14, 'add_voteuser');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (54, 'Can change vote user', 14, 'change_voteuser');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (55, 'Can delete vote user', 14, 'delete_voteuser');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (56, 'Can view vote user', 14, 'view_voteuser');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (57, 'Can add vote record', 15, 'add_voterecord');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (58, 'Can change vote record', 15, 'change_voterecord');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (59, 'Can delete vote record', 15, 'delete_voterecord');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (60, 'Can view vote record', 15, 'view_voterecord');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (61, 'Can add payment record', 16, 'add_paymentrecord');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (62, 'Can change payment record', 16, 'change_paymentrecord');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (63, 'Can delete payment record', 16, 'delete_paymentrecord');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (64, 'Can view payment record', 16, 'view_paymentrecord');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (65, 'Can add feedback', 17, 'add_feedback');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (66, 'Can change feedback', 17, 'change_feedback');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (67, 'Can delete feedback', 17, 'delete_feedback');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (68, 'Can view feedback', 17, 'view_feedback');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (69, 'Can add apply prize', 18, 'add_applyprize');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (70, 'Can change apply prize', 18, 'change_applyprize');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (71, 'Can delete apply prize', 18, 'delete_applyprize');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (72, 'Can view apply prize', 18, 'view_applyprize');
COMMIT;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (7, 'main', 'active');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (18, 'main', 'applyprize');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (8, 'main', 'domain');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (17, 'main', 'feedback');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (9, 'main', 'logs');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (10, 'main', 'officialaccount');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (16, 'main', 'paymentrecord');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (11, 'main', 'token');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (12, 'main', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (13, 'main', 'voteactivity');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (15, 'main', 'voterecord');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (14, 'main', 'voteuser');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (6, 'sessions', 'session');
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1, 'contenttypes', '0001_initial', '2023-02-27 09:20:25.291513');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (2, 'auth', '0001_initial', '2023-02-27 09:20:25.649912');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (3, 'admin', '0001_initial', '2023-02-27 09:20:25.740824');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2023-02-27 09:20:25.752807');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2023-02-27 09:20:25.763679');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2023-02-27 09:20:25.817542');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2023-02-27 09:20:25.926286');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (8, 'auth', '0003_alter_user_email_max_length', '2023-02-27 09:20:25.970211');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (9, 'auth', '0004_alter_user_username_opts', '2023-02-27 09:20:25.983181');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (10, 'auth', '0005_alter_user_last_login_null', '2023-02-27 09:20:26.022541');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (11, 'auth', '0006_require_contenttypes_0002', '2023-02-27 09:20:26.027744');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2023-02-27 09:20:26.039839');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (13, 'auth', '0008_alter_user_username_max_length', '2023-02-27 09:20:26.080298');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2023-02-27 09:20:26.117743');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (15, 'auth', '0010_alter_group_name_max_length', '2023-02-27 09:20:26.151548');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (16, 'auth', '0011_update_proxy_permissions', '2023-02-27 09:20:26.167268');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2023-02-27 09:20:26.204170');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (18, 'main', '0001_initial', '2023-02-27 09:20:26.755171');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (19, 'sessions', '0001_initial', '2023-02-27 09:20:26.848372');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (20, 'main', '0002_voteactivity_name', '2023-02-28 01:26:08.897916');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (21, 'main', '0003_auto_20230228_0211', '2023-02-28 02:11:43.811594');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (22, 'main', '0004_auto_20230228_0400', '2023-02-28 04:00:47.063989');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (23, 'main', '0005_auto_20230228_0539', '2023-02-28 05:39:31.766579');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (24, 'main', '0006_auto_20230228_0842', '2023-02-28 08:42:54.480060');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (25, 'main', '0007_auto_20230228_0929', '2023-02-28 09:30:06.363603');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (26, 'main', '0008_alter_voteactivity_img', '2023-03-01 06:26:15.324191');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (27, 'main', '0009_auto_20230301_0829', '2023-03-01 08:29:45.949169');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (28, 'main', '0010_auto_20230301_0831', '2023-03-01 08:32:01.095463');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (29, 'main', '0011_auto_20230302_0111', '2023-03-02 01:12:06.979930');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (30, 'main', '0012_auto_20230302_0159', '2023-03-02 01:59:49.549196');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (31, 'main', '0013_voteactivity_vote_voteusers', '2023-03-02 03:37:02.581722');
COMMIT;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of django_session
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for main_active
-- ----------------------------
DROP TABLE IF EXISTS `main_active`;
CREATE TABLE `main_active` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `domain_list` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_active
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for main_applyprize
-- ----------------------------
DROP TABLE IF EXISTS `main_applyprize`;
CREATE TABLE `main_applyprize` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(8) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `create_time` int NOT NULL,
  `status` int NOT NULL,
  `voteuser_id` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_applyprize_voteuser_id_4915b451_fk_main_voteuser_open_id` (`voteuser_id`),
  CONSTRAINT `main_applyprize_voteuser_id_4915b451_fk_main_voteuser_open_id` FOREIGN KEY (`voteuser_id`) REFERENCES `main_voteuser` (`open_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_applyprize
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for main_domain
-- ----------------------------
DROP TABLE IF EXISTS `main_domain`;
CREATE TABLE `main_domain` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `domain_name` varchar(50) NOT NULL,
  `status` int NOT NULL,
  `visit_count` int NOT NULL,
  `expire_time` int NOT NULL,
  `flow` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain_name` (`domain_name`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_domain
-- ----------------------------
BEGIN;
INSERT INTO `main_domain` (`id`, `domain_name`, `status`, `visit_count`, `expire_time`, `flow`) VALUES (92, 'www.yangjie.com', 0, 0, 1672540200, 0);
INSERT INTO `main_domain` (`id`, `domain_name`, `status`, `visit_count`, `expire_time`, `flow`) VALUES (94, 'www.123123.com', 1, 0, 1672547400, 0);
INSERT INTO `main_domain` (`id`, `domain_name`, `status`, `visit_count`, `expire_time`, `flow`) VALUES (95, 'www.tabcom.com', 1, 0, 1591773300, 0);
COMMIT;

-- ----------------------------
-- Table structure for main_feedback
-- ----------------------------
DROP TABLE IF EXISTS `main_feedback`;
CREATE TABLE `main_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `create_time` int NOT NULL,
  `voteuser_id` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_feedback_voteuser_id_ec094971_fk_main_voteuser_open_id` (`voteuser_id`),
  CONSTRAINT `main_feedback_voteuser_id_ec094971_fk_main_voteuser_open_id` FOREIGN KEY (`voteuser_id`) REFERENCES `main_voteuser` (`open_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_feedback
-- ----------------------------
BEGIN;
INSERT INTO `main_feedback` (`id`, `content`, `create_time`, `voteuser_id`) VALUES (1, 'thaslfew', 0, 'wxxiaotest');
INSERT INTO `main_feedback` (`id`, `content`, `create_time`, `voteuser_id`) VALUES (2, 'fasdfasd', 0, 'wxxiaotest');
COMMIT;

-- ----------------------------
-- Table structure for main_logs
-- ----------------------------
DROP TABLE IF EXISTS `main_logs`;
CREATE TABLE `main_logs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `who` varchar(20) NOT NULL,
  `action` longtext NOT NULL,
  `target` longtext NOT NULL,
  `create_time` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_logs
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for main_officialaccount
-- ----------------------------
DROP TABLE IF EXISTS `main_officialaccount`;
CREATE TABLE `main_officialaccount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `officialcount_name` longtext NOT NULL,
  `app_id` longtext NOT NULL,
  `region` longtext NOT NULL,
  `wxpay_pos_id` longtext NOT NULL,
  `wxpay_apiv2_secret_key` longtext NOT NULL,
  `wxpay_apiv3_secret_key` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_officialaccount
-- ----------------------------
BEGIN;
INSERT INTO `main_officialaccount` (`id`, `officialcount_name`, `app_id`, `region`, `wxpay_pos_id`, `wxpay_apiv2_secret_key`, `wxpay_apiv3_secret_key`) VALUES (1, '华强0.', '111', '111', '111', '111', '111');
COMMIT;

-- ----------------------------
-- Table structure for main_paymentrecord
-- ----------------------------
DROP TABLE IF EXISTS `main_paymentrecord`;
CREATE TABLE `main_paymentrecord` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `price` decimal(5,2) NOT NULL,
  `create_time` int NOT NULL,
  `ip` longtext NOT NULL,
  `phone_number` longtext NOT NULL,
  `system` longtext NOT NULL,
  `network` longtext NOT NULL,
  `vote_activity_id` int NOT NULL,
  `voteuser_id` varchar(128) NOT NULL,
  `payment_order_id` longtext NOT NULL DEFAULT (_utf8mb3''),
  `payment_status` int NOT NULL,
  `prize_type` longtext NOT NULL DEFAULT (_utf8mb3''),
  `phone_model` longtext NOT NULL DEFAULT (_utf8mb3''),
  PRIMARY KEY (`id`),
  KEY `main_paymentrecord_vote_activity_id_83615c22_fk_main_vote` (`vote_activity_id`),
  KEY `main_paymentrecord_voteuser_id_07100654_fk_main_voteuser_open_id` (`voteuser_id`),
  CONSTRAINT `main_paymentrecord_vote_activity_id_83615c22_fk_main_vote` FOREIGN KEY (`vote_activity_id`) REFERENCES `main_voteactivity` (`vote_id`),
  CONSTRAINT `main_paymentrecord_voteuser_id_07100654_fk_main_voteuser_open_id` FOREIGN KEY (`voteuser_id`) REFERENCES `main_voteuser` (`open_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_paymentrecord
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for main_token
-- ----------------------------
DROP TABLE IF EXISTS `main_token`;
CREATE TABLE `main_token` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `value` varchar(32) NOT NULL,
  `expire_time` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `value` (`value`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_token
-- ----------------------------
BEGIN;
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (45, 'sy0MrPzkShFCKawBG3d2H7D8e1YTxm5t', 1678333395);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (46, 'j4tHbhguNS3Q6zqIkEcXZ1OCLM057xYy', 1678333444);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (47, 'wgqY1DfPmayiKG3StLbCeEAWzxoMOk6s', 1678333472);
COMMIT;

-- ----------------------------
-- Table structure for main_user
-- ----------------------------
DROP TABLE IF EXISTS `main_user`;
CREATE TABLE `main_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `username` varchar(20) NOT NULL,
  `pwd` varchar(64) NOT NULL,
  `create_time` int NOT NULL,
  `last_login_time` int NOT NULL,
  `email` varchar(50) NOT NULL,
  `auth` int NOT NULL,
  `avator` longtext NOT NULL,
  `token` varchar(32) NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_user
-- ----------------------------
BEGIN;
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `token`, `status`) VALUES (1, '杨杰', 'yangjie', 'f6fdffe48c908deb0f4c3bd36c032e72', 1677544354, 1677728595, '1654040434@qq.com', 1, '22', 'sy0MrPzkShFCKawBG3d2H7D8e1YTxm5t', 1);
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `token`, `status`) VALUES (2, 'lly', 'liliyu', 'f6fdffe48c908deb0f4c3bd36c032e72', 1677656242, 1677728672, 'isliliyu@gmail.com', 1, '26', 'wgqY1DfPmayiKG3StLbCeEAWzxoMOk6s', 1);
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `token`, `status`) VALUES (3, '老王', 'laowang', 'f6fdffe48c908deb0f4c3bd36c032e72', 1677661657, 1677728644, 'caro1xxxhv@gmail.com', 1, '22', 'j4tHbhguNS3Q6zqIkEcXZ1OCLM057xYy', 1);
COMMIT;

-- ----------------------------
-- Table structure for main_voteactivity
-- ----------------------------
DROP TABLE IF EXISTS `main_voteactivity`;
CREATE TABLE `main_voteactivity` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `vote_id` int NOT NULL,
  `flow` int NOT NULL,
  `share` int NOT NULL,
  `img` varchar(100) NOT NULL,
  `income` int NOT NULL,
  `create_time` int NOT NULL,
  `expire_time` int NOT NULL,
  `create_user_id` varchar(20) NOT NULL,
  `domain_id` varchar(50) NOT NULL,
  `name` longtext NOT NULL DEFAULT (_utf8mb3''),
  `allowed_alone_everyday_vote_count` int NOT NULL,
  `allowed_vote_region` longtext NOT NULL DEFAULT (_utf8mb3''),
  `visit_count` int NOT NULL,
  `visit_count_multiple` int NOT NULL,
  `vote_enroll_begin_time` int NOT NULL,
  `vote_enroll_end_time` int NOT NULL,
  `vote_everyday_begin_time` int NOT NULL,
  `vote_everyday_end_time` int NOT NULL,
  `allowed_alone_everyhour_vote_count` int NOT NULL,
  `enable_comment` int NOT NULL,
  `enable_vote_cert_code` int NOT NULL,
  `enable_vote_to_me` int NOT NULL,
  `open_today_star_with` int NOT NULL,
  `today_star_update_begin_time` int NOT NULL,
  `today_star_update_end_time` int NOT NULL,
  `today_start_voteuser_id` varchar(128) DEFAULT NULL,
  `visible_no1_with` int NOT NULL,
  `vote_count_restrict` longtext NOT NULL DEFAULT (_utf8mb3''),
  `auto_comment_begin_time` int NOT NULL,
  `auto_comment_end_time` int NOT NULL,
  `auto_comment_everyday_begin_time` int NOT NULL,
  `auto_comment_everyday_count_strict` int NOT NULL,
  `auto_comment_everyday_end_time` int NOT NULL,
  `auto_comment_space_minute` int NOT NULL,
  `auto_comment_voteuser_id` varchar(128) DEFAULT NULL,
  `enable_browser` int NOT NULL,
  `enable_prize` int NOT NULL,
  `template_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vote_id` (`vote_id`),
  KEY `main_voteactivity_create_user_id_ec0e666e_fk_main_user_username` (`create_user_id`),
  KEY `main_voteactivity_domain_id_2aab4b4b_fk_main_domain_domain_name` (`domain_id`),
  KEY `main_voteactivity_today_start_voteuser_7e4576ce_fk_main_vote` (`today_start_voteuser_id`),
  KEY `main_voteactivity_auto_comment_voteuse_d865bef7_fk_main_vote` (`auto_comment_voteuser_id`),
  CONSTRAINT `main_voteactivity_auto_comment_voteuse_d865bef7_fk_main_vote` FOREIGN KEY (`auto_comment_voteuser_id`) REFERENCES `main_voteuser` (`open_id`),
  CONSTRAINT `main_voteactivity_create_user_id_ec0e666e_fk_main_user_username` FOREIGN KEY (`create_user_id`) REFERENCES `main_user` (`username`),
  CONSTRAINT `main_voteactivity_domain_id_2aab4b4b_fk_main_domain_domain_name` FOREIGN KEY (`domain_id`) REFERENCES `main_domain` (`domain_name`),
  CONSTRAINT `main_voteactivity_today_start_voteuser_7e4576ce_fk_main_vote` FOREIGN KEY (`today_start_voteuser_id`) REFERENCES `main_voteuser` (`open_id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_voteactivity
-- ----------------------------
BEGIN;
INSERT INTO `main_voteactivity` (`id`, `vote_id`, `flow`, `share`, `img`, `income`, `create_time`, `expire_time`, `create_user_id`, `domain_id`, `name`, `allowed_alone_everyday_vote_count`, `allowed_vote_region`, `visit_count`, `visit_count_multiple`, `vote_enroll_begin_time`, `vote_enroll_end_time`, `vote_everyday_begin_time`, `vote_everyday_end_time`, `allowed_alone_everyhour_vote_count`, `enable_comment`, `enable_vote_cert_code`, `enable_vote_to_me`, `open_today_star_with`, `today_star_update_begin_time`, `today_star_update_end_time`, `today_start_voteuser_id`, `visible_no1_with`, `vote_count_restrict`, `auto_comment_begin_time`, `auto_comment_end_time`, `auto_comment_everyday_begin_time`, `auto_comment_everyday_count_strict`, `auto_comment_everyday_end_time`, `auto_comment_space_minute`, `auto_comment_voteuser_id`, `enable_browser`, `enable_prize`, `template_id`) VALUES (54, 201349, 0, 0, 'img/logo.png', 0, 1679932800, 1680537600, 'liliyu', 'www.123123.com', 'huodong', 0, '', 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL, 0, '[]', 0, 0, 0, 0, 0, 0, NULL, 0, 0, 0);
INSERT INTO `main_voteactivity` (`id`, `vote_id`, `flow`, `share`, `img`, `income`, `create_time`, `expire_time`, `create_user_id`, `domain_id`, `name`, `allowed_alone_everyday_vote_count`, `allowed_vote_region`, `visit_count`, `visit_count_multiple`, `vote_enroll_begin_time`, `vote_enroll_end_time`, `vote_everyday_begin_time`, `vote_everyday_end_time`, `allowed_alone_everyhour_vote_count`, `enable_comment`, `enable_vote_cert_code`, `enable_vote_to_me`, `open_today_star_with`, `today_star_update_begin_time`, `today_star_update_end_time`, `today_start_voteuser_id`, `visible_no1_with`, `vote_count_restrict`, `auto_comment_begin_time`, `auto_comment_end_time`, `auto_comment_everyday_begin_time`, `auto_comment_everyday_count_strict`, `auto_comment_everyday_end_time`, `auto_comment_space_minute`, `auto_comment_voteuser_id`, `enable_browser`, `enable_prize`, `template_id`) VALUES (55, 849612, 0, 0, 'img/logo_dknGQr2.png', 0, 1679932800, 1680537600, 'liliyu', 'www.123123.com', 'huodong', 0, '', 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL, 0, '[]', 0, 0, 0, 0, 0, 0, NULL, 0, 0, 0);
INSERT INTO `main_voteactivity` (`id`, `vote_id`, `flow`, `share`, `img`, `income`, `create_time`, `expire_time`, `create_user_id`, `domain_id`, `name`, `allowed_alone_everyday_vote_count`, `allowed_vote_region`, `visit_count`, `visit_count_multiple`, `vote_enroll_begin_time`, `vote_enroll_end_time`, `vote_everyday_begin_time`, `vote_everyday_end_time`, `allowed_alone_everyhour_vote_count`, `enable_comment`, `enable_vote_cert_code`, `enable_vote_to_me`, `open_today_star_with`, `today_star_update_begin_time`, `today_star_update_end_time`, `today_start_voteuser_id`, `visible_no1_with`, `vote_count_restrict`, `auto_comment_begin_time`, `auto_comment_end_time`, `auto_comment_everyday_begin_time`, `auto_comment_everyday_count_strict`, `auto_comment_everyday_end_time`, `auto_comment_space_minute`, `auto_comment_voteuser_id`, `enable_browser`, `enable_prize`, `template_id`) VALUES (56, 723850, 0, 0, 'img/logo_IKkBg66.png', 0, 1679932800, 1680537600, 'liliyu', 'www.123123.com', 'huodong', 0, '', 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL, 0, '[]', 0, 0, 0, 0, 0, 0, NULL, 0, 0, 0);
COMMIT;

-- ----------------------------
-- Table structure for main_voterecord
-- ----------------------------
DROP TABLE IF EXISTS `main_voterecord`;
CREATE TABLE `main_voterecord` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` int NOT NULL,
  `vote_activity_id` int NOT NULL,
  `voteuser_id` varchar(128) NOT NULL,
  `ip` longtext NOT NULL DEFAULT (_utf8mb3''),
  `network` longtext NOT NULL DEFAULT (_utf8mb3''),
  `phone_number` longtext NOT NULL DEFAULT (_utf8mb3''),
  `system` longtext NOT NULL DEFAULT (_utf8mb3''),
  `phone_model` longtext NOT NULL DEFAULT (_utf8mb3''),
  PRIMARY KEY (`id`),
  KEY `main_voterecord_vote_activity_id_afb04140_fk_main_vote` (`vote_activity_id`),
  KEY `main_voterecord_voteuser_id_b27d8380_fk_main_voteuser_open_id` (`voteuser_id`),
  CONSTRAINT `main_voterecord_vote_activity_id_afb04140_fk_main_vote` FOREIGN KEY (`vote_activity_id`) REFERENCES `main_voteactivity` (`vote_id`),
  CONSTRAINT `main_voterecord_voteuser_id_b27d8380_fk_main_voteuser_open_id` FOREIGN KEY (`voteuser_id`) REFERENCES `main_voteuser` (`open_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_voterecord
-- ----------------------------
BEGIN;
INSERT INTO `main_voterecord` (`id`, `create_time`, `vote_activity_id`, `voteuser_id`, `ip`, `network`, `phone_number`, `system`, `phone_model`) VALUES (19, 0, 849612, 'wxxiaotest', '0.0.0.0', 'wifi', '17723948948', 'ios', 'iphone');
INSERT INTO `main_voterecord` (`id`, `create_time`, `vote_activity_id`, `voteuser_id`, `ip`, `network`, `phone_number`, `system`, `phone_model`) VALUES (20, 0, 849612, 'wxxiaotest', '0.0.0.0', 'wifi', '1893274', 'android', 'andriod');
COMMIT;

-- ----------------------------
-- Table structure for main_voteuser
-- ----------------------------
DROP TABLE IF EXISTS `main_voteuser`;
CREATE TABLE `main_voteuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `open_id` varchar(128) NOT NULL,
  `wx_username` longtext NOT NULL,
  `create_time` int NOT NULL,
  `avator` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `open_id` (`open_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of main_voteuser
-- ----------------------------
BEGIN;
INSERT INTO `main_voteuser` (`id`, `open_id`, `wx_username`, `create_time`, `avator`) VALUES (1, 'wxxiaotest', 'exname', 0, '0');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
