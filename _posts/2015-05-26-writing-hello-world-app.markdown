---
layout: post
title:  "Writing Helloworld app"
date:   2015-05-26
comments: true
---

<p class="intro">
    <span class="dropcap">T</span>
    his page will guide you how to write application for the Front End Website (Common module).
</p>

CONTROLLER LAYER
----
Create a file called ***HelloWorldController.php*** and placed in the directory ***/modules/common/controllers*** with the following content:

{% highlight php startinline=true %}
<?php
namespace Controller\Common;

class HelloworldController extends \Fly\BaseController
{
    public funtion initialize()
    {
        parent::initialize();
    }

    public function indexAction()
    {
        $myApp = new \Model\HelloWorld();
        $hello = $myApp->getHello();
        $world = $myApp->getWorld();

        $this->tag->prependTitle('Hello World App');
        $this->view->setVars([
            'helloworld' => $hello . ' ' . $world
        ]);
    }
}
{% endhighlight %}

MODEL LAYER
----
Create a file called ***HelloWorld.php*** and placed in the directory ***/Models/*** with the following content:

{% highlight php startinline=true %}
<?php
namespace Model;

class HelloWorld extends \Fly\BaseModel
{
    public $hello;
    public $world;

    public function initialize()
    {
        parent::initialize();
    }

    public function getHello()
    {
        return $this->hello;
    }

    public function getWorld()
    {
        return $this->world;
    }
}
{% endhighlight %}

VIEW LAYER
----
Create a folder ***/modules/common/views/default/helloworld*** and create file named ***index.volt*** in the folder you just created with content:

{% highlight html %}
{% raw %}
{% extends "layouts/main.volt" %}
{% block content %}
    {{ helloworld }}
{% endblock %}
{% endraw %}
{% endhighlight %}

AUTHORIZATION
----
Before running the HelloWorld App, you need to authorize one particular User group. If you see in the content of the file named ***Module.php*** placed in folder ***/modules/common/*** one line look like below then Access Control List already opened and you must be grant a permission for that controller just created. If not, you can ignore this step.

{% highlight php startinline=true %}
$eventManager->attach('dispatch', new \Fly\Authorization('common'));
{% endhighlight %}

Examples here granted permission for group Guest can access a wealth helloworld controller and the index action.
Open file named ***permission.php*** placed in ***/conf/*** then add the following content:

{% highlight php startinline=true %}
<?php

/**
 * Access Controll List (ACL) Config Variable for Core Framework
 * @var array
 */
define('ROLE_GUEST', 1);
define('ROLE_ADMIN', 5);
define('ROLE_MOD', 10);
define('ROLE_MEMBER', 15);

return [
    ROLE_GUEST => [
        'Admin' => array (
            'login:*',
            'notfound:*',
        ),
        'Common' => array (
            'index:*',
            'install:*',
            'helloworld:*', //line added after create helloworld controller
        ),
    ],
{% endhighlight %}

If you already logged in as Administrator, you must add permissions for ***ROLE_ADMIN*** be able to access the helloworld app.

Now, you can access the functions you've written in the path ***http://localhost/phalcon-jumpstart/helloworld***