---
layout: post
title:  "Phalcon Jumpstart - Modules Structure"
date:   2015-05-26
description: Controller Layer is a key component in getting the required treatment, navigate, distribute and call proper Model and View to complete 1 Request.
comments: true
---

<p class="intro">
    <span class="dropcap">C</span>
    ontroller Layer is a key component in getting the required treatment, navigate, distribute and call proper Model and View to complete 1 Request.
</p>

In order to limit the construction of separate treatment groups for the website (back-end, front-end, ...) because when constructing one particular group in the classic way, the system must rebuild one almost similar. For example, to build the system administrator (Back-end), the classic way must copy the framework and put in one directory with full admin system folders, files such as Front-End Web.

With the new design, the system administrator or any one system is added later, just create a directory with the name of the module. Default Module (Front-End) called Common and all of its controller file will be created in the directory ***/modules/common/*** .

Module class declare in ***/conf/global.php***

{% highlight php startinline=true %}
//Array variable to register modules in application container
$modules = [
    'app_modules' => [
        'common'   => [
            'className' => 'Module\Common',
            'path'      => ROOT_PATH . '/modules/common/Module.php',
        ],
        'admin' => [
            'className' => 'Module\Admin',
            'path'      => ROOT_PATH . '/modules/admin/Module.php'
        ],
        'mobile' => [
            'className' => 'Module\Mobile',
            'path'      => ROOT_PATH . '/modules/mobile/Module.php'
        ]
    ]
];
{% endhighlight %}

Now if you want to add functionality Admin (Back-End) with its own controller system, just create one folder named by module, eg directory ***/modules/admin*** , then you've got an Admin module . Now just go to this directory and create corresponding controller to handle the admin function is finished.
The name of the module will help identify the controllers within its class, because the Framework uses automated systems should include the name of the Controller file class declaration must be declared namespace ***Controller/YOUR_MODULE***

Example declare the Product controller in Admin module with CRUD:

{% highlight php startinline=true %}
<?php
namespace Controller\Admin;

class ProductController extends \Fly\BaseController
{
    public function initialize()
    {
        parent::initialize();
    }

    public function indexAction()
    {
        //Product listing
    }

    public function createAction()
    {
        //Create a new Product
    }

    public function editAction()
    {
        //Edit existed Product
    }

    public function deleteAction()
    {
        //Delete existed Product
    }
}
{% endhighlight %}