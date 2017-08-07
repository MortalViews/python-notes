"""
<div>
    <div>
    <span>
    <t>Hi, sanjay</t>
    </span>
    </div>
</div>
"""
"""
<div>
<t>
<span>
Hi,sanjay
</span>
<t>
<div>
"""
from tags import title,span,div

name="sanjay"

@div
@title
@div
@span
def say_hi(name):
    return "HI %s"%(name)

say_hi= div(title(div(span(say_hi))))


def say_bye(name):
    return "Bye %s"%(name)


email_say_hi = div(div(title(span(say_hi))))


logout_say_bye=div(title(span(say_bye)))