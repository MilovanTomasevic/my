class: center, middle

## {{ title }}
{% if subtitle %}### {{ subtitle }}{% endif %}
{% if subsubtitle %}#### {{ subsubtitle }}{% endif %}

.author[{{ author }}]

.small[{{ affiliation }}]

{% if unfinished %}
.small[Slajdovi u izradi]
{% endif %}

.created[{{now|dtformat("%d.%m.%Y u %H:%M")}}]


---
{% block slides %}{% endblock %}
