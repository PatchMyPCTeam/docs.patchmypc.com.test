---
description: >-
  Granting Advanced Insights a role in ConfigMgr. Not required for Patch
  Insights.
---

# Insights Configuration Manager Permission requirements

_Applies to: Patch My PC Advanced and Patch Insights_

For various Configuration Manager **console actions** and **features** to work, the accounts running the IIS App Pools need to have permissions to connect to your SMS Provider Server.&#x20;

![](../_images/Permissions%20Example.png%20"Highlighted%20actions%20all%20require%20permission%20on%20your%20SMS%20Provider%20Server")

{% hint style="info" %}
Note: If you installed Advanced Insights on an SMS Provider Server then you may not have to configure any permissions for this to work.
{% endhint %}

By default, the **IIS App Pools** run under the local computer account of your Advanced Insights Server.&#x20;

![](../_images/image%20%281320%29.png%20"")

***

### ⚙ Add the IIS Pool Account To ConfigMgr Security Role

1. Open the ConfigMgr console and navigate to **Administration** > **Security** > **Administrative Users** > click **Add User or Group**
2. Choose the User/Computer account running your IIS App Pools. In our example we are adding the local computer account of our server named "SCCM"
3. Assign them the **Operations Administrator** role[ (or optionally a custom role)](insights-configuration-manager-permission-requirements.md#use-a-custom-security-role-optional)

![](../_images/image%20%281095%29.png%20"")

***

### ⚙ Use a Custom Security Role (<mark style="color:yellow;">Optional</mark>)

If you wish to adhere to the "Principle of Least Privilege" then you can download the XML file below and import it as a security role into ConfigMgr. This role grants the lowest possible privileges.

{% file src="../_images/Patch%20My%20PC%20Advanced%20Insights%20Client%20Actions%20and%20Collections%20%281%29.zip" %}

To import the security role XML file, open the ConfigMgr console and navigate to **Administration** > **Security** > **Security Roles** > click **Import Security Role**.

![](../_images/image%20%281163%29.png%20"")

***

### ⚙Allow RPC traffic (<mark style="color:yellow;">If using remote server</mark>)

If you are using a remote Advanced Insights server there are these requirements to use any console actions or features:

* The Remote Procedure Call (RPC) service must be running
* Firewall must allow RPC Traffic (TCP ports: **135**, **RPC dynamic ports (49152–65535)**

Details on how to configure a firewall rule to allow this traffic can be found here:&#x20;

[https://learn.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista](https://learn.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista)
