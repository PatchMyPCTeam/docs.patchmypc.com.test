# Using Entra ID Security Groups in Cloud

_Applies to: Patch My PC Cloud_

Patch My PC (PMPC) Cloud supports the use of Entra ID Security Groups to control who has access to your PMPC Cloud company and which actions they can perform.

Once the Entra ID Security Groups feature has been enabled for your PMPC Cloud Company and provided you have successfully connected it to your Intune tenant, you will see the **Entra ID Groups** tab under the **Users** node.

{% hint style="danger" %}
**Important**

If the Entra ID domain used to sign in on our portal differs from that used in the Intune tenant connected to our portal, we do not allow sign-in using Entra ID group role assignments as we cannot match the domains.
{% endhint %}

<figure><img src="/_images/gitbook/image%20%282255%29.png" alt="“Entra ID Groups” tab on the “Users” node"><figcaption></figcaption></figure>

Using Entra ID Security Groups feature of PMPC Cloud allows you to:

* [Add an Entra ID Security Group](add-an-entra-id-group-to-cloud.md)
* [View an Entra ID Security Group's Membership](view-an-entra-id-groups-membership-in-cloud.md)
* [Modify an Entra ID Security Group](modify-an-entra-id-group-in-cloud.md)
* [Remove an Entra ID Security Group](remove-an-entra-id-group-from-cloud.md)

{% hint style="info" %}
**Note**

The following actions cannot be performed with PMPC Cloud and need to be performed from within Entra ID:

* Modifying the membership of a group (add or remove).
* Moving users between groups.
* Deleting groups from Entra ID.

Also, when you first set up a PMPC Cloud company, the user creating the company is automatically assigned the **Full Admin with Access Management** role. To avoid access issues (such as this user leaving your company and not passing on their credentials/setting up another user with this role), we recommend you either:

* [Add a second user](../add-a-cloud-user.md) and assign them this role.
* [Add an Entra ID Security Group](add-an-entra-id-group-to-cloud.md) to the portal and assign it the **Full Admin with Access Management** role.

Once you’ve done this, we recommend you use Entra ID Security Groups to manage any additional users who need to have access to your PMPC Cloud company.
{% endhint %}
