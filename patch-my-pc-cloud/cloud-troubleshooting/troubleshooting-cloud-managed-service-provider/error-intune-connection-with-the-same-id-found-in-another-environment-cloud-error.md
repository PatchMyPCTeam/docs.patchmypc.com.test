# “Error - Intune connection with the same Id found in another environment!” Cloud error

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I am trying to create a child Patch My PC (PMPC) Cloud company using the Managed Service Provider (MSP) feature.

However, after clicking **Connect** and authenticating, I get the following error:

**Error**

**Intune connection with the same Id found in another environment!**

<figure><img src="/_images/gitbook/image%20%282094%29.png" alt="“Intune connection with the same Id found in another environment!” error" width="538"><figcaption></figcaption></figure>

### CAUSE

This is because the Intune tenant you are trying to connect is already in use by another company, probably because the child company already exists.

We do not support sharing an Intune tenant between multiple PMPC Cloud companies.

### RESOLUTION

Sign in to the child company and navigate to  **Settings | Environments** and if Intune is already connected, delete the connection.

{% hint style="info" %}
**Note**

See [Deleting an Intune tenant connection](../../cloud-administration/manage-your-environments-in-cloud/manage-cloud-intune-tenants.md#deleting-an-intune-tenant-connection) for more information.
{% endhint %}
