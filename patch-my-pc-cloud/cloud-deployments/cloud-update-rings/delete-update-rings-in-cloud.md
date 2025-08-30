# Delete Update Rings in Cloud

_Applies to: Patch My PC Cloud_

For a Patch My PC (PMPC) Cloud deployment with Update Rings enabled, you can either:

* [Delete all Update Rings](delete-update-rings-in-cloud.md#delete-all-update-rings)
* [Delete a Single Update Ring](delete-update-rings-in-cloud.md#delete-a-single-update-ring)

{% hint style="info" %}
**Note**

All deletion tasks for Update Rings are performed from the **Assignments** tab of the respective deployment.
{% endhint %}

### Delete all Update Rings

To delete all Update Rings for a deployment:

1. [Edit](../manage-cloud-deployments/edit-a-cloud-deployment.md) the relevant deployment and navigate to the **Assignments** tab.
2.  If you want to delete a single Update Ring, use the [Delete a Single Update Ring](delete-update-rings-in-cloud.md#delete-a-single-update-ring) process.\
    \
    To delete all Update Rings for this deployment, click **Remove all Rings**.\


    ![Clicking “Remove all Rings”](../../../_images/image%20%282061%29.png%20"Clicking%20\"Remove%20all%20Rings\"")


3.  On the **Move Assignments or Delete** dialog box, click **Move** to remove the Update Rings but keep all the existing assignments.\
    \


    ![Clicking “Move” to remove the Update Rings but keep all the existing assignments](../../../_images/image%20%282062%29.png%20"Clicking%20\"Move\"%20to%20remove%20the%20Update%20Rings%20but%20keep%20all%20the%20existing%20assignments")

{% hint style="info" %}
**Note**

Clicking **Delete** will delete any existing assignments but not the deployment itself.

![Clicking “Delete” will delete any existing assignments, not the deployment itself.](../../../_images/image%20%282064).png>)\

{% endhint %}

The Update Rings are removed and any existing assignments are kept.

![Update Rings are removed and any existing assignments are kept](../../../_images/image%20%282065%29.png%20"Update%20Rings%20are%20removed%20and%20any%20existing%20assignments%20are%20kept")

4.  Click **Save** to save your changes.\
    \


    ![Clicking “Save” to save changes](../../../_images/image%20%282066%29.png%20"Clicking%20\"Save\"%20to%20save%20changes")

{% hint style="warning" %}
**Important**

As removing all Update Rings disables Update Ring functionality for this deployment (which could result in unintended results), the **"**_**\<deployment\_name>**_**" Deployment Summary** is shown detailing the impact of your proposed change.\
\
For example, this version of the app will be deployed immediately to all of the following assignments without any of the delays enforced by using Update Rings.

![“Deployment Summary” showing the impact of deleting all Update Rings ](../../../_images/image%20%282067).png>)
{% endhint %}

{% hint style="info" %}
**Note**

If the existing deployment had different versions applied to different assignments, we use the version that was applied to the lowest delay ring before the deployment was edited.
{% endhint %}

5.  Click **Cancel** to return to the **Assignments** tab to make any required changes, or click **Confirm** to save your changes.\
    \
    The **Deployments** node is displayed along with the **Success – Edited <**_**deployment\_name**_**>** notification.\
    \


    ![“Deployment Summary” showing the impact of delete all Update Rings](../../../_images/image%20%282068%29.png%20"\"Deployment%20Summary\"%20showing%20the%20impact%20of%20delete%20all%20Update%20Rings")

{% hint style="success" %}
**Tip**

If you edit the deployment and click **More Info**, you will see the tabs representing the Update Rings are no longer present.
{% endhint %}

### Delete a Single Update Ring

To delete a Single Update Ring:

1. Navigate to the **Assignments** page of the deployment.
2. Click the red **X** beside the Update Ring you want to delete.

{% hint style="info" %}
**Note**

Deleting an Update Ring also deletes any assignments controlled by that ring. If you want to keep the assignment, drag and drop it to another ring before you delete the ring.
{% endhint %}

![Clicking the read “X” to delete a specific Update Ring](../../../_images/image%20%282069%29.png%20"Clicking%20the%20read%20\"X\"%20to%20delete%20a%20specific%20Update%20Ring")

The ring and any assignments it contains are deleted.

![Update Ring deleted](../../../_images/image%20%282070%29.png%20"Update%20Ring%20deleted")

3.  Click **Save** to save your changes.\
    \


    ![Clicking “Save” to save changes](../../../_images/image%20%282071%29.png%20"Clicking%20\"Save\"%20to%20save%20changes")

    \
    As you’ve removed an Update Ring and it’s assignments, the **"<**_**deployment\_name**_**>" Deployment Summary** is shown detailing the impact of your proposed change.\
    \
    For example, by deleting the **7-Zip Pilot +7 Days** ring, this app will not be deployed to the **03 - Patching - Production - All - 7 Days** Entra ID group.\
    \


    ![“Deployment Summary” showing the impact of deleting this Update Rings](../../../_images/image%20%282072%29.png%20"\"Deployment%20Summary\"%20showing%20the%20impact%20of%20deleting%20this%20Update%20Rings")
4.  Click **Cancel** to return to the **Assignments** tab to make any required changes, or click **Confirm** to save your changes.\
    \
    The **Deployments** node is displayed along with the **Success – Edited <**_**deployment\_name**_**>** notification.\


    ![“Deployment Summary” showing the impact of delete all Update Rings](../../../_images/image%20%282073%29.png%20"\"Deployment%20Summary\"%20showing%20the%20impact%20of%20delete%20all%20Update%20Rings")

{% hint style="success" %}
**Tip**

If you edit the deployment and click **More Info**, you will see the tab representing the deleted Update Ring is no longer present.
{% endhint %}
