# Why don’t I see the “Discovery” node in the Cloud portal?

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I have signed into the Patch My PC (PMPC) Cloud portal, but I don’t see the **Discovery** node.

<figure><img src="../../../_images/gitbook/image%20%28526%29.png" alt="No “Discovery” node" width="305"><figcaption></figcaption></figure>

### CAUSE

This is because your portal is not connected to an Intune tenant.

{% hint style="info" %}
**Note**

Not having an Intune tenant connected will also prevent other nodes such as the **Notifications** node from appearing.
{% endhint %}

### RESOLUTION

To resolve this issue, follow the [Connecting to an Intune tenant](../../cloud-administration/manage-your-environments-in-cloud/manage-cloud-intune-tenants.md#connecting-to-an-intune-tenant) section of the [Managing Intune tenants](../../cloud-administration/manage-your-environments-in-cloud/manage-cloud-intune-tenants.md) process.

Once your portal has been connected to an Intune tenant you will see the **Discovery** node.

<figure><img src="../../../_images/gitbook/image%20%28527%29.png" alt="“Discovery” node now visible" width="271"><figcaption></figcaption></figure>
