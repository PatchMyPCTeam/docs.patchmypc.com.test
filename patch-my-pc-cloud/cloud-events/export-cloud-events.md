# Export Cloud Events

_Applies to: Patch My PC Cloud_

{% hint style="warning" %}
**Important**

Events are only held in the portal for 30 days, after which they are automatically groomed from the database. If you wish to keep events longer than 30 days, you need to export them.
{% endhint %}

To export today's events plus the past 29 days of events, click **Export** in the header of the **Events** page.

![](/_images/image-(1772 "").png "")

{% hint style="info" %}
**Note**

The number in parentheses beside the **Export** button shows how many events will be exported.
{% endhint %}

A CSV file called **events\_log\_entries.csv** is downloaded to your computer. This contains the number of entries shown in parentheses and can then serve as an archive or be imported to another application for onward manipulation.

We export the following:

* Date
* Title
* Architecture
* &#x20;Installer Type
* User
* Category
* Operation
* Type
* Version
* Description

Here is an example:

![](/_images/image-(97 "").png "")

{% hint style="success" %}
**Tip**

You can use Filters to control which events you export, rather than exporting all events. See [Filter Events](filter-cloud-events.md) for more information.
{% endhint %}
