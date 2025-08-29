# Categories (Deployments)

_Applies to: Patch My PC Cloud_

{% hint style="info" %}
**Note**

Using the **Categories** tool is optional.
{% endhint %}

The **Categories** tool of the Patch My PC (PMPC) Cloud deployment wizard allows you to leverage Intune App Categories (Categories) in your deployments to help users find apps in the Company Portal.

{% hint style="info" %}
**Note**

See the [Create and edit categories for apps](https://learn.microsoft.com/en-us/mem/intune/apps/apps-add#create-and-edit-categories-for-apps) section of [Add apps to Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/apps/apps-add) for more information on App Categories.
{% endhint %}

To add a Category to a deployment:

1. Click the **Categories** tool.

<figure><img src="/_images/gitbook/image%20%2872%29.png" alt="Clicking the “Categories” tool" width="563"><figcaption></figcaption></figure>

2. Scroll down to the **Categories** section.

<figure><img src="/_images/gitbook/image%20%2873%29.png" alt="Scrolling down to the &#x22;Categories&#x22; section" width="563"><figcaption></figcaption></figure>

3. Go to Step 6. to add a new category or in the **Add Category** field, either:
   1. Start typing the name of the relevant Category, then click the checkbox beside it to select it.
   2. Click the dropdown to see a list of existing Categories and click the relevant checkbox(es) to select it.

<figure><img src="/_images/gitbook/image%20%2874%29.png" alt="Selecting the checkbox beside the relevant categories" width="421"><figcaption></figcaption></figure>

{% hint style="success" %}
**Tip**

You can click the **X** beside a Category in the **Add Category** field to delete it from the list.
{% endhint %}

4. Repeat this process to add any additional categories.
5. Go to to step 8. if you do not want to add a new Category.
6. To add a new Category, type its name in the **Add Category** field.

{% hint style="info" %}
**Note**

You can create up to 200 categories per Intune tenant. Each category name must:

* Be unique
* Be less than 255 characters
* Not contain the backslash (**\\**) or quote (**"**) characters
* Not be the name of a script.
{% endhint %}

<figure><img src="/_images/gitbook/image%20%2875%29.png" alt=""><figcaption></figcaption></figure>

7. Press `ENTER` and the **Success – The category “<**_**category\_name>**_**” has been created** notification is shown, confirming the new category has been added to both Intune and this deployment.

<figure><img src="/_images/gitbook/image%20%2876%29.png" alt="“Success – The category “<category_name>” has been created” notification" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**

See [Check App Categories](../../../cloud-reference/intune-reference/check-app-categories-in-intune.md) for details on how to check within Intune that the Categories defined in the deployment have been assigned correctly.

Also:

* If different Categories are configured in the portal and Intune admin center they are combined to be the same.
* If a Category is created in the portal and then removed from the Intune admin center, it will be re-added by the portal.
* Categories are also copied forward to a new version of an app.
{% endhint %}

8. If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab.\
   \
   Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant process.

<figure><img src="/_images/gitbook/image%20%2877%29.png" alt="Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page" width="563"><figcaption></figcaption></figure>
