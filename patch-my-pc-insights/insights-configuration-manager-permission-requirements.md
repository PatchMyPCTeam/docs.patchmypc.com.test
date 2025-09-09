---
description: >-
  Granting Advanced Insights a role in ConfigMgr. Not required for Patch
  Insights.
---

# Insights Configuration Manager Permission requirements

_Applies to: Patch My PC Advanced and Patch Insights_

For various Configuration Manager <strong>console actions</strong> and <strong>features</strong> to work, the accounts running the IIS App Pools need to have permissions to connect to your SMS Provider Server.&#x20;

![](/_images/Permissions-Example.png)

<blockquote class="wp-block-quote">
<p>Note: If you installed Advanced Insights on an SMS Provider Server then you may not have to configure any permissions for this to work.</p>
</blockquote>

By default, the <strong>IIS App Pools</strong> run under the local computer account of your Advanced Insights Server.&#x20;

![](/_images/image-(1320).png "")

<strong>*

### ⚙ Add the IIS Pool Account To ConfigMgr Security Role

1. Open the ConfigMgr console and navigate to </strong>Administration<strong> > </strong>Security<strong> > </strong>Administrative Users<strong> > click </strong>Add User or Group<strong>
2. Choose the User/Computer account running your IIS App Pools. In our example we are adding the local computer account of our server named "SCCM"
3. Assign them the </strong>Operations Administrator<strong> role[ (or optionally a custom role)](insights-configuration-manager-permission-requirements.md#use-a-custom-security-role-optional)

![](/_images/image-(1095).png "")

</strong>*

### ⚙ Use a Custom Security Role (<mark style="color:yellow;">Optional</mark>)

If you wish to adhere to the "Principle of Least Privilege" then you can download the XML file below and import it as a security role into ConfigMgr. This role grants the lowest possible privileges.

{% file src="..//_images/Patch My PC Advanced Insights Client Actions and Collections (1).zip" %}

To import the security role XML file, open the ConfigMgr console and navigate to <strong>Administration</strong> > <strong>Security</strong> > <strong>Security Roles</strong> > click <strong>Import Security Role</strong>.

![](/_images/image-(1163).png "")

<strong>*

### ⚙Allow RPC traffic (<mark style="color:yellow;">If using remote server</mark>)

If you are using a remote Advanced Insights server there are these requirements to use any console actions or features:

* The Remote Procedure Call (RPC) service must be running
* Firewall must allow RPC Traffic (TCP ports: </strong>135<strong>, </strong>RPC dynamic ports (49152–65535)**

Details on how to configure a firewall rule to allow this traffic can be found here:&#x20;

[https://learn.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista](https://learn.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista)