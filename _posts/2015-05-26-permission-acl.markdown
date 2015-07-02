---
layout: post
title:  "Phalcon Jumpstart - Access Control List"
date:   2015-05-26
description: Phalcon\Acl provides an easy and lightweight management of ACLs as well as the permissions attached to them. Access Control Lists (ACL) allow an application to control access to its areas and the underlying objects from requests. You are encouraged to read more about the ACL methodology so as to be familiar with its concepts.
comments: true
---

<p class="intro">
    <span class="dropcap">P</span>
    halcon\Acl provides an easy and lightweight management of ACLs as well as the permissions attached to them. Access Control Lists (ACL) allow an application to control access to its areas and the underlying objects from requests. You are encouraged to read more about the ACL methodology so as to be familiar with its concepts.
</p>

Phalcon\Acl provides an easy and lightweight management of ACLs as well as the permissions attached to them. Access Control Lists (ACL) allow an application to control access to its areas and the underlying objects from requests. You are encouraged to read more about the ACL methodology so as to be familiar with its concepts.

In summary, ACLs have roles and resources. Resources are objects which abide by the permissions defined to them by the ACLs. Roles are objects that request access to resources and can be allowed or denied access by the ACL mechanism.

Authorization
----

Active ACL in each module with following code:

{% highlight php startinline=true %}
/**
 * File: /modules/admin/Module.php
 */
public function registerServices($di)
{
    $eventManager->attach('dispatch', new \Fly\Authorization('admin'));
}
{% endhighlight %}

Before execute route, class \Fly\Authorization will be call, that step will be check session to get user role information for verify which area that user can access or no.

For better performance, i store acl object serialize data in ***/cache/security/acl.data*** file, u can change it to APC or memcached for faster than disk I/O.

User role and permission stored in ***/conf/permission.php*** file like below

{% highlight php startinline=true %}
<?php

/**
 * Access Controll List (ACL) Config Variable for Core Framework
 * @var array
 */
define('ROLE_GUEST', 1);

return [
    ROLE_GUEST => [
        'Admin' => array (
            'login:*',
            'notfound:*',
        ),
        'Common' => array (
            'index:*',
        ),
    ],
    ...
];
{% endhighlight %}

* **ROLE\_GUEST**: user group define with value, example: ROLE\_ADMIN, ROLE\_MEMBER, ...
* **Admin, Common**: define what modules user have permission.
* **login, notfound, index, install**: controller what user have permission.
* *: what action user can execute.
    * **\***: all Action
    * For example, if you want user of group Guest only run index Action and add Action on Product controller of Admin module, declare like below:

{% highlight php startinline=true %}
ROLE_GUEST => array (
    'Admin' => array(
        'product:index',
        'product:add'
    )
)
{% endhighlight %}

When user access to area which user did not permission, user will be redirect to notfound controller.

