---
layout: post
title:  "Phalcon Jumpstart - Directory Structure"
date:   2015-05-26
description: Introduction to directory structure in Phalcon Jumpstart Framework.
comments: true
---

***/models/*** - all of model classes in the Framework MVC pattern.

***/modules/*** - core class of each module and folder of controller,view.

***/modules/admin/controllers/*** - classes for controllers in Admin module.

***/modules/common/controllers/*** - classes for controllers in Common module.

***/modules/mobile/controllers/*** - classes for mobile redirect controllers in Mobile module.

***/modules/admin/views/*** - Each controller will have one folder of the same name with the controller, containing the corresponding .volt file for action of Admin module

***/modules/common/views/*** - Each controller will have one folder of the same name with the controller, containing the corresponding .volt file for action of Common module

***/modules/mobile/views/*** - Each controller will have one folder of the same name with the controller, containing the corresponding .volt file for action of Mobile module

***/libs/Fly/*** - core classes of Phalcon Jumpstart DevTool.

***/libs/League/*** - files manager library.

***/libs/Phalcon/*** - extra Phalcon library.

***/libs/Whoops/*** - exception handler library.

***/conf/*** - contain global config and permission of framework.

***/cli/*** - console environment of Phalcon Micro Application.

***/cache/annotations/*** - contain files of phalcon model annotations caching.

***/cache/metadata/*** - contain files of  phalcon model metadata caching.

***/cache/minified/*** - caching files of css/js minifier library.

***/cache/security/*** - access control list serialize object caching.

***/cache/volt/*** - contains template files after they have been translated (.php) and saved by the mechanism of Volt Template Engine.

***/language/en/admin/*** - English language for Admin module.

***/language/en/common/*** - English language for Common module.

***/logs/app/*** - user custom log of webapp.

***/logs/mig/*** - sql query log of db migrate task.

***/migration/*** - contain JSON file using to create table structure & data from migrate task.

***/public/css/*** - contains the CSS file

***/public/js/*** - contains the javascript file

***/public/images/*** - contain images

***/public/min/*** - Library CSS/JS minify to minify CSS and JavaScript files, file configuration in /public/min/groupsConfig.php

***/public/plugins/*** - third party front-end library.

***/public/uploads/*** - contain the files uploaded by the system.
