---
layout: post
title:  "Phalcon Jumpstart - Views Structure"
date:   2015-05-26
description: View Layer by Framework layer is the interface, display of the site. View Layer enables applications using the correct interface for the respective functions of the website.
comments: true
---

<p class="intro">
    <span class="dropcap">V</span>
    iew Layer by Framework layer is the interface, display of the site. View Layer enables applications using the correct interface for the respective functions of the website.
</p>

View Layer by Framework layer is the interface, display of the site. View Layer enables applications using the correct interface for the respective functions of the website.

To add a template file (.volt files), first need to determine whether the current Controller Module, so that put .volt file to the correct folder (***/modules/{{MODULE_NAME}}/views/{{CONTROLLER_NAME}}/***). or you can custom loading view layouts specified in each ***Module.php*** file placed in based modules directory.

{% highlight php startinline=true %}
$di['view']->setViewsDir(ROOT_PATH . '/modules/admin/views/');
{% endhighlight %}

Next to specify the name of the template file. The file name is usually the same name as the action is called and there is .volt extension. Example: Create a template for Create action into Product controller of Admin module , you should create a template file ***/modules/admin/views/product/create.volt***

Example for default controller view template structure:

{% highlight html %}
{% raw %}
{% extends "layouts/main.volt" %}

{% block content %}
    Welcome to Phalcon Jumpstart DevTool
{% endblock %}
{% endraw %}
{% endhighlight %}