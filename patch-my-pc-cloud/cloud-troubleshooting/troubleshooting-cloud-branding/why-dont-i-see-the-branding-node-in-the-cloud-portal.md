# Why don’t I see the “Branding” node in the Cloud portal?

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I have signed into the Patch My PC (PMPC) Cloud portal, but I don’t see the **Branding** node under **Settings**.

![No &#x22;Branding&#x22; node](/_images/image-(1570).png "No &#x22;Branding&#x22; node")

### CAUSE

This is because your portal is not connected to an Intune tenant.

{% hint style="info" %}
**Note**

Not having an Intune tenant connected will also prevent the **Notifications** node from appearing.
{% endhint %}

### RESOLUTION

To resolve this issue, follow the [Connecting to an Intune tenant](../../cloud-administration/manage-your-environments-in-cloud/manage-cloud-intune-tenants.md#connecting-to-an-intune-tenant) section of the [Managing Intune tenants](../../cloud-administration/manage-your-environments-in-cloud/manage-cloud-intune-tenants.md) process.

Once your portal has been connected to an Intune tenant you will see the **Branding** node.

![&#x22;Branding&#x22; node is now visible](/_images/image-(1571).png "&#x22;Branding&#x22; node is now visible")