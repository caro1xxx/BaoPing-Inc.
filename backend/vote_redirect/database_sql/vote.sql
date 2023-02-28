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

 Date: 27/02/2023 15:26:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (25, 'Can add user', 7, 'add_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (26, 'Can change user', 7, 'change_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (27, 'Can delete user', 7, 'delete_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (28, 'Can view user', 7, 'view_user');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (29, 'Can add logs', 8, 'add_logs');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (30, 'Can change logs', 8, 'change_logs');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (31, 'Can delete logs', 8, 'delete_logs');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (32, 'Can view logs', 8, 'view_logs');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (33, 'Can add token', 9, 'add_token');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (34, 'Can change token', 9, 'change_token');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (35, 'Can delete token', 9, 'delete_token');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (36, 'Can view token', 9, 'view_token');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (37, 'Can add official account', 10, 'add_officialaccount');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (38, 'Can change official account', 10, 'change_officialaccount');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (39, 'Can delete official account', 10, 'delete_officialaccount');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (40, 'Can view official account', 10, 'view_officialaccount');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (41, 'Can add vote user', 11, 'add_voteuser');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (42, 'Can change vote user', 11, 'change_voteuser');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (43, 'Can delete vote user', 11, 'delete_voteuser');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (44, 'Can view vote user', 11, 'view_voteuser');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (45, 'Can add feedback', 12, 'add_feedback');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (46, 'Can change feedback', 12, 'change_feedback');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (47, 'Can delete feedback', 12, 'delete_feedback');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (48, 'Can view feedback', 12, 'view_feedback');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (49, 'Can add active', 13, 'add_active');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (50, 'Can change active', 13, 'change_active');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (51, 'Can delete active', 13, 'delete_active');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (52, 'Can view active', 13, 'view_active');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (53, 'Can add domain', 14, 'add_domain');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (54, 'Can change domain', 14, 'change_domain');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (55, 'Can delete domain', 14, 'delete_domain');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (56, 'Can view domain', 14, 'view_domain');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (57, 'Can add vote activity', 15, 'add_voteactivity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (58, 'Can change vote activity', 15, 'change_voteactivity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (59, 'Can delete vote activity', 15, 'delete_voteactivity');
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (60, 'Can view vote activity', 15, 'view_voteactivity');
COMMIT;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (13, 'main', 'active');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (14, 'main', 'domain');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (12, 'main', 'feedback');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (8, 'main', 'logs');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (10, 'main', 'officialaccount');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (9, 'main', 'token');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (7, 'main', 'user');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (15, 'main', 'voteactivity');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (11, 'main', 'voteuser');
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (6, 'sessions', 'session');
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1, 'contenttypes', '0001_initial', '2023-02-22 02:36:25.805762');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (2, 'auth', '0001_initial', '2023-02-22 02:36:28.433677');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (3, 'admin', '0001_initial', '2023-02-22 02:36:29.135389');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2023-02-22 02:36:29.219556');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2023-02-22 02:36:29.300857');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2023-02-22 02:36:29.744165');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2023-02-22 02:36:29.955609');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (8, 'auth', '0003_alter_user_email_max_length', '2023-02-22 02:36:30.094314');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (9, 'auth', '0004_alter_user_username_opts', '2023-02-22 02:36:30.176212');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (10, 'auth', '0005_alter_user_last_login_null', '2023-02-22 02:36:30.366526');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (11, 'auth', '0006_require_contenttypes_0002', '2023-02-22 02:36:30.445204');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2023-02-22 02:36:30.528049');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (13, 'auth', '0008_alter_user_username_max_length', '2023-02-22 02:36:30.732029');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2023-02-22 02:36:30.964247');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (15, 'auth', '0010_alter_group_name_max_length', '2023-02-22 02:36:31.101824');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (16, 'auth', '0011_update_proxy_permissions', '2023-02-22 02:36:31.286803');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2023-02-22 02:36:31.502902');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (18, 'main', '0001_initial', '2023-02-22 02:36:31.942520');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (19, 'sessions', '0001_initial', '2023-02-22 02:36:32.250453');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (20, 'main', '0002_auto_20230222_0630', '2023-02-22 06:31:57.324063');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (21, 'main', '0003_alter_user_email', '2023-02-23 03:36:48.949647');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (22, 'main', '0004_alter_user_avator', '2023-02-23 07:17:16.368404');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (23, 'main', '0005_alter_user_avator', '2023-02-23 07:25:42.338622');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (24, 'main', '0006_auto_20230224_0233', '2023-02-24 02:33:50.620360');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (25, 'main', '0007_auto_20230224_0247', '2023-02-24 02:48:05.286571');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (26, 'main', '0008_alter_user_token', '2023-02-24 07:06:44.776779');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (27, 'main', '0009_alter_user_token', '2023-02-24 07:16:03.390721');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (28, 'main', '0010_token', '2023-02-24 07:18:04.799819');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (29, 'main', '0011_auto_20230227_0107', '2023-02-27 01:08:18.023151');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (30, 'main', '0012_voteuser', '2023-02-27 01:47:31.894410');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (31, 'main', '0013_auto_20230227_0206', '2023-02-27 02:07:13.168840');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (32, 'main', '0014_active_domain_voteactivity', '2023-02-27 03:05:01.305592');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (33, 'main', '0015_alter_feedback_open_id', '2023-02-27 03:53:14.124848');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (34, 'main', '0016_alter_feedback_open_id', '2023-02-27 04:58:59.794165');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (35, 'main', '0017_rename_open_id_feedback_voteuser', '2023-02-27 05:03:45.954666');
COMMIT;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `domain_list` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_active
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for main_domain
-- ----------------------------
DROP TABLE IF EXISTS `main_domain`;
CREATE TABLE `main_domain` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `domain` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `status` int NOT NULL,
  `vis_cnt` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_domain
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for main_feedback
-- ----------------------------
DROP TABLE IF EXISTS `main_feedback`;
CREATE TABLE `main_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` int NOT NULL,
  `voteuser_id` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_feedback_voteuser_id_ec094971_fk_main_voteuser_open_id` (`voteuser_id`),
  CONSTRAINT `main_feedback_voteuser_id_ec094971_fk_main_voteuser_open_id` FOREIGN KEY (`voteuser_id`) REFERENCES `main_voteuser` (`open_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_feedback
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for main_logs
-- ----------------------------
DROP TABLE IF EXISTS `main_logs`;
CREATE TABLE `main_logs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `who` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `action` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `target` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_logs
-- ----------------------------
BEGIN;
INSERT INTO `main_logs` (`id`, `who`, `action`, `target`, `create_time`) VALUES (1, 'xiaotest', '042361', 'newadmin', 1677206638);
INSERT INTO `main_logs` (`id`, `who`, `action`, `target`, `create_time`) VALUES (2, 'xiaotest', '042361', 'newadmin', 1677207653);
INSERT INTO `main_logs` (`id`, `who`, `action`, `target`, `create_time`) VALUES (3, 'xiaotest', '042361', 'newadmin', 1677207661);
INSERT INTO `main_logs` (`id`, `who`, `action`, `target`, `create_time`) VALUES (4, 'xiaotest', '042361', 'newadmin', 1677207716);
INSERT INTO `main_logs` (`id`, `who`, `action`, `target`, `create_time`) VALUES (5, 'xiaotest', '042361', 'newadmin', 1677207729);
COMMIT;

-- ----------------------------
-- Table structure for main_officialaccount
-- ----------------------------
DROP TABLE IF EXISTS `main_officialaccount`;
CREATE TABLE `main_officialaccount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `app_id` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `region` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `wx_pay_pos_id` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `wx_pay_apiv2_secret_key` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `wx_pay_apiv3_secret_key` longtext COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_officialaccount
-- ----------------------------
BEGIN;
INSERT INTO `main_officialaccount` (`id`, `name`, `app_id`, `region`, `wx_pay_pos_id`, `wx_pay_apiv2_secret_key`, `wx_pay_apiv3_secret_key`) VALUES (1, 'text11111', '5235afdr32', 'Shanghai', '4te4gvdsf23a', '5432hsd3253fed', '534fw3456fs');
COMMIT;

-- ----------------------------
-- Table structure for main_token
-- ----------------------------
DROP TABLE IF EXISTS `main_token`;
CREATE TABLE `main_token` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `value` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  `expire_time` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `main_token_value_1766c531_uniq` (`value`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_token
-- ----------------------------
BEGIN;
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (1, '5kJtQBUx4vuLlCcNMOI0871RWzDgnTHP', 1677223811);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (2, 'jUs4WEAm5XyODVa02zZhtwxLBNb8T9Rr', 1677225147);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (3, '8cl937E1ohDrYUnwkgTAyX5PI0FpsNit', 1677235436);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (4, 'dnDasNEeFyuO1g8KSmC0cZtvibXHW3h7', 1677236317);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (5, 'aPAiHt4NEcqbLFuKwIZ2MsW10YrnvzOl', 1677236897);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (6, 'kA9Qj0wyaeTst2huDJRZISVMF61HfEnm', 1977299218);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (7, 'h0iLxzKyDbZCAJg9m3Yd8BWRrsHQtEvG', 1977469627);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (8, '9snNuIYM5lRpHv4zSqZLVWUa0dygOeCD', 1677469840);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (9, 'cBFpnkv4AytgreoL0hx35T6EamCuKw9D', 1677470002);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (10, 'xDy9rwkJBpf6YNbnHGztXh4sljS5cFPC', 1677482872);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (11, 'IzZLKl3Q9qvRyMPJdbUHaVSuXFwgW5fA', 1677485173);
INSERT INTO `main_token` (`id`, `value`, `expire_time`) VALUES (12, 'eS4atjF98worCRhEBMd0lsxgbzG7KmpI', 1677487654);
COMMIT;

-- ----------------------------
-- Table structure for main_user
-- ----------------------------
DROP TABLE IF EXISTS `main_user`;
CREATE TABLE `main_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `username` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `pwd` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` int NOT NULL,
  `last_login_time` int NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `auth` int NOT NULL,
  `avator` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `status` int NOT NULL,
  `token` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `main_user_email_2597293b_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_user
-- ----------------------------
BEGIN;
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (5, 'liliyu', 'lack', 'f6fdffe48c908deb0f4c3bd36c032e72', 1677057571, 1677057571, 'lack@gmail.com', 1, '1', 1, 'OoZnVXKJE2Pk36ic');
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (7, 'liliyu', 'xiaobai', 'f6fdffe48c908deb0f4c3bd36c032e72', 1677057723, 1677057723, 'xiaobai@email.com', 1, '1', 1, 'Bk6wbX4VPnpzOJl3');
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (8, 'liliyu', 'admin', 'f6fdffe48c908deb0f4c3bd36c032e72', 1677057753, 1677215951, 'll@email.com', 0, '1', 1, 'b\'YWRtaW4gMTY3NzIxNTk1MQ==\'');
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (11, 'xiaohua', 'xiaohua', 'c0cda4a45b403dec993afa9879d58b87', 1677128607, 1677128607, 'isl@gmail.com', 1, '1', 1, '6kSb7DGATRIwvPf5');
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (12, 'xiaohua', 'xiaosha', 'c0cda4a45b403dec993afa9879d58b87', 1677129153, 1677129153, 'u@gmail.com', 1, '1', 1, 'HqmaAZ2kNVxpKysX');
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (13, 'xiaoxiao', 'xiaotest', '80396443f055ea0c4fd9719ecefcc25a', 1677129464, 1677477574, 'isliliyu@gmail.com', 1, '1', 1, 'eS4atjF98worCRhEBMd0lsxgbzG7KmpI');
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (29, 'name', 'username', 'pwd', 1231, 123123, 'create_time', 1, '1', 1, 'token');
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (45, 'newname', 'xiaot', 'f6fdffe48c908deb0f4c3bd36c032e72', 1677228889, 0, 'ifdsfs@gmail.com', 1, '1', 1, '-');
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (46, 'newname', 'xiatt', 'f6fdffe48c908deb0f4c3bd36c032e72', 1677229888, 0, 'ifsf@gmail.com', 1, '1', 1, '-');
INSERT INTO `main_user` (`id`, `name`, `username`, `pwd`, `create_time`, `last_login_time`, `email`, `auth`, `avator`, `status`, `token`) VALUES (47, 'newname', 'xidasat', '220466675e31b9d20c051d5e57974150', 1677229906, 0, 'ifsf@mail.com', 1, '1', 0, '-');
COMMIT;

-- ----------------------------
-- Table structure for main_voteuser
-- ----------------------------
DROP TABLE IF EXISTS `main_voteuser`;
CREATE TABLE `main_voteuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `open_id` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `wx_username` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `create_time` int NOT NULL,
  `avator` longtext COLLATE utf8mb4_general_ci NOT NULL DEFAULT (_utf8mb3''),
  PRIMARY KEY (`id`),
  UNIQUE KEY `open_id` (`open_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of main_voteuser
-- ----------------------------
BEGIN;
INSERT INTO `main_voteuser` (`id`, `open_id`, `wx_username`, `create_time`, `avator`) VALUES (1, 'wx_xiaotest', 'xiaotest', 120347047, '1');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
