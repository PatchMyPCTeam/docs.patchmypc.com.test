# Manage Cloud Intune tenants

_Applies to: Patch My PC Cloud_

The Patch My PC (PMPC) Cloud portal allows you to connect to an Intune tenant. You can also delete the connection and connect to a different tenant if required.

* [Connecting to an Intune tenant](manage-cloud-intune-tenants.md#connecting-to-an-intune-tenant)
* [Reconnecting an Intune tenant](manage-cloud-intune-tenants.md#reconnecting-an-intune-tenant)
* [Deleting an Intune tenant connection](manage-cloud-intune-tenants.md#deleting-an-intune-tenant-connection)

### Connecting to an Intune tenant

To connect your portal to a new Intune tenant:

1.  Navigate to **Settings | Environments**.\


    ![](/_images/image-(1732 "").png "")


2. Under the **Intune** tab, click **Connect**

![](/_images/image-(2701 "").png "")

3. Enter the Entra ID you used to onboard to PMPC Cloud or click to select the relevant account from the list of already signed-in accounts. Then click **Next**.

![](/_images/image-(1472 "").png "")



4.  Enter the password and click **Sign in**.

    ![](/_images/image-(1473 "").png "")


5. On the **Permissions requested** screen, click **Accept**.

{% hint style="info" %}
**Note**

You must have the **Global Administrator** role in Entra ID to approve our enterprise app.

We require these permissions to connect with your Intune tenant.

See [Permissions required for the Intune Apps](../../cloud-reference/cloud-permissions-reference/permissions-required-for-intune-apps.md) for more details.
{% endhint %}

![](/_images/image-(341 "").png "")

{% hint style="success" %}
**Tip**

You can click the down arrow beside each permission to get more information.
{% endhint %}

6. On the next screen, verify that there is a green tick above the **Intune Tenant Connected Successfully** section.

![](/_images/image-(2705 "").png "")

7. If you have purchased a license key, go to Step 10.
8. If you want to start a free 30-day trial, enter the number of devices you want to use during your trial in the **Enter total number of managed devices in production** checkbox, then click **Start Now**.&#x20;

![](/_images/image-(2707 "").png "")

The **You have successfully activated your license** dialog box is displayed on which you can click **Close**

![](/_images/image-(2708 "").png "")

A countdown will be shown during your trial showing the number of days left on the trial. Once your trial expires, you will see the **Your license has expired** notification.

![](/_images/image-(2709 "").png "")

9. To purchase a license, click **Request a Quote** in the notification, which will redirect to you to our quote form where you can request a quote for buying the number of licenses you require.
10. If you already have a valid license key, type it in the **Enter License Key Here** field and click **Activate Now**.

![](/_images/image-(2710 "").png "")

The **You have successfully activated your license** dialog box is displayed on which you can click **Close**

![](/_images/image-(2711 "").png "")

11. Click **App Catalog** to see all of the applications that can be deployed and managed using Intune Apps for Cloud.

![](/_images/image-(1736 "").png "")

### Reconnecting an Intune tenant

If your portal loses its connection to your Intune tenant (for example, if a Global Admin revokes the [Permissions required for Intune Apps](../../cloud-reference/cloud-permissions-reference/permissions-required-for-intune-apps.md) from within Intune), you can use the **Reconnect** button to re-establish the connection to your previously connected Intune tenant, which will re-grant the required permissions.

{% hint style="info" %}
**Note**

The **Reconnect** button is only available once an Intune connection has been established.

You will only be able to reconnect to an Intune tenant you’ve previously connected to, based on the tenant ID we have stored in the portal’s database.
{% endhint %}

To reconnect your portal to an Intune tenant you’ve previously connected to:

1.  Navigate to **Settings | Environments**.\


    ![](/_images/image-(1738 "").png "")


2. Click **Reconnect** under your **Intune** tenant.

![](/_images/image-(2570 "").png "")

3. Enter the Entra ID you used to onboard to PMPC Cloud or click to select the relevant account from the list of already signed-in accounts. Then click **Next**.\


![](/_images/image-(772 "").png "")

4. Enter the password and click **Sign in**.

![](/_images/image-(773 "").png "")

5. On the **Permission requested** screen, click Accept.\


![](/_images/image-(774 "").png "")



6. Click on the **Events** node to check for the **Intune Connection Added** event, confirming that the Intune connection was restored.

![](/_images/image-(775 "").png "")

### Deleting an Intune tenant connection

{% hint style="warning" %}
**Important**

If you disconnect Intune from your PMPC Cloud Company, any added Entra ID Security Groups will be removed and lose access to your PMPC Cloud Company, and the **Add Group** button will no longer appear.
{% endhint %}

To delete a connection to an Intune tenant from your portal:

1.  Navigate to **Settings | Environments**.\


    ![](/_images/image-(1686 "").png "")


2. On the **Environments** page, click **Delete** underneath **Intune**.

![](/_images/image-(2571 "").png "")

3. On the **Are you sure you want to disconnect Intune** dialog box, read the message to understand the implications, then click **OK** to continue.

{% hint style="danger" %}
**Warning**

Disconnecting an Intune tenant will delete all:

* Deployments which, for those with a [Retention Policy](../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/retention-policy-deployments.md) defined,  will include the latest and all old unassigned versions of all deployments.
* Banners
* Notifications

There is no undo for this action.
{% endhint %}

![](/_images/image-(1688 "").png "")

The text underneath the **Intune** section changes to **Connect** followed by the **Success - Intune  disconnected** notification.

![](/_images/image-(2572 "").png "")
