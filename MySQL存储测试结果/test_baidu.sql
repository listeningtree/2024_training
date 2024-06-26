/*
Navicat MySQL Data Transfer

Source Server         : MySQL80
Source Server Version : 80017
Source Host           : localhost:3306
Source Database       : test_baidu

Target Server Type    : MYSQL
Target Server Version : 80017
File Encoding         : 65001

Date: 2024-06-26 16:33:06
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for test_result_save
-- ----------------------------
DROP TABLE IF EXISTS `test_result_save`;
CREATE TABLE `test_result_save` (
  `test_case_id` varchar(100) NOT NULL,
  `test_case_name` varchar(150) NOT NULL,
  `test_task_id` varchar(100) NOT NULL,
  `test_task_name` varchar(150) NOT NULL,
  `interface_test_result` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `UI_test_result` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`test_case_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of test_result_save
-- ----------------------------
INSERT INTO `test_result_save` VALUES ('0101', '输入100以内个字符（不包括100字符），可以正常输入,正常搜索', '01', '输入框字符长度限制效果测试', 'pass', 'pass');
INSERT INTO `test_result_save` VALUES ('0102', '输入100字符，可以正常输入，正常搜索', '01', '输入框字符长度限制效果测试', 'pass', 'pass');
INSERT INTO `test_result_save` VALUES ('0103', '输入超过100字符（如：101字符），超过100字符部分无法正常输入，搜索只搜索前面100字符', '01', '输入框字符长度限制效果测试', 'fail', 'fail');
INSERT INTO `test_result_save` VALUES ('0104', '输入为空，不跳转搜索结果页，回到初始搜索界面', '01', '输入框字符长度限制效果测试', 'pass', 'pass');
INSERT INTO `test_result_save` VALUES ('0105', '特殊字符测试：输入空格，不跳转搜索结果页，回到初始搜索页', '01', '输入框字符长度限制效果测试', 'pass', 'pass');
INSERT INTO `test_result_save` VALUES ('0201', '输入20以内个字符（不包括20字符），点击百度一下按钮，返回关于输入的所有字符的搜索结果界面', '02', '搜索内容只截取前20个字符功能测试', 'pass', 'pass');
INSERT INTO `test_result_save` VALUES ('0202', '输入20个字符，点击百度一下按钮，返回关于输入的20个字符的搜索结果界面', '02', '搜索内容只截取前20个字符功能测试', 'pass', 'pass');
INSERT INTO `test_result_save` VALUES ('0203', '输入超过20个字符，点击百度一下按钮，返回关于所输入字符的前20个字符的搜索结果界面', '02', '搜索内容只截取前20个字符功能测试', 'fail', 'fail');
INSERT INTO `test_result_save` VALUES ('0301', '输入不包含<和>的20以内个字符，点击百度一下按钮返回关于输入的所有字符的搜索结果界面', '03', '搜索内容自动去除”<“和”>“字符功能测试', 'pass', 'pass');
INSERT INTO `test_result_save` VALUES ('0302', '输入包含一个<的20以内个字符，点击百度一下按钮，返回关于去除<的输入字符的搜索结果界面', '03', '搜索内容自动去除”<“和”>“字符功能测试', 'fail', 'fail');
INSERT INTO `test_result_save` VALUES ('0303', '输入包含两个<的20以内个字符，点击百度一下按钮，返回关于去除<的输入字符的搜索结果界面', '03', '搜索内容自动去除”<“和”>“字符功能测试', 'fail', 'fail');
INSERT INTO `test_result_save` VALUES ('0304', '输入包含一个>的20以内个字符，点击百度一下按钮，返回关于去除所有>的输入字符的搜索结果界面', '03', '测试任务名称：搜索内容自动去除”<“和”>“字符功能测试', 'fail', 'fail');
INSERT INTO `test_result_save` VALUES ('0305', '输入包含两个>的20以内个字符，点击百度一下按钮，返回关于去除所有>的输入字符的搜索结果界面', '03', '搜索内容自动去除”<“和”>“字符功能测试', 'fail', 'fail');
INSERT INTO `test_result_save` VALUES ('0306', '输入包含一个<和一个>的20以内个字符，点击百度一下按钮，返回关于去除>和<的输入字符的搜索结果界面', '03', '搜索内容自动去除”<“和”>“字符功能测试', 'fail', 'fail');
