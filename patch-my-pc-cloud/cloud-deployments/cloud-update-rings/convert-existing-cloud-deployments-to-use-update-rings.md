# Convert Existing Cloud Deployments to use Update Rings

_Applies to: Patch My PC Cloud_

If you have already successfully deployed an app using Patch My PC (PMPC) Cloud, you can convert that deployment to use Update Rings.

To convert an existing deployment to use Update Rings:

1.  [Edit the deployment](../manage-cloud-deployments/edit-a-cloud-deployment.md) and navigate to the **Assignments** tab.\


    <figure><img src="../../../_images/gitbook/image (449).png" alt="Navigating to the “Assignments” tab"><figcaption></figcaption></figure>

    \
    Any existing assignments for the deployment are shown.\


    <figure><img src="../../../_images/gitbook/image (450).png" alt="Existing assignments"><figcaption></figcaption></figure>
2.  Click **Enable Update Rings**.\


    <figure><img src="../../../_images/gitbook/image (451).png" alt="Clicking “Enable Update Rings”"><figcaption></figcaption></figure>
3.  On the **Move Assignments or Delete** dialog box, click **Move** to create the Update Rings and move any existing assignments to the first Update Ring.\


    <figure><img src="../../../_images/gitbook/image (452).png" alt="Clicking “Move” to move any existing assignments to the first Update Ring." width="450"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**

Clicking **Delete** will delete any existing assignments, not the deployment itself. It will also create the default two Update Rings with default settings.
{% endhint %}

Any existing assignments are moved into the first Update Ring.

<figure><img src="../../../_images/gitbook/image (2046).png" alt="Any existing assignments are moved into the first Update Ring."><figcaption></figcaption></figure>

4. Continue from Step 3 of the [Create Update Rings](create-update-rings-in-cloud.md) process to configure your Update Rings. For example, adding additional assignments, moving assignments between rings, etc.
5.  Once you have completed reconfiguring the deployment, click **Save**.\
    \


    <figure><img src="../../../_images/gitbook/image (454).png" alt="Clicking “Save” to save changes"><figcaption></figcaption></figure>

The deployment will be updated and the Update Rings will be created depending on the type of rings you chose ([Delayed](how-cloud-update-rings-are-created.md#delayed-update-rings) or [Immediate](how-cloud-update-rings-are-created.md#immediate-update-rings)).
