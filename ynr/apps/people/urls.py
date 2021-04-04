from django.conf.urls import url

import candidates.views as views

urlpatterns = [
    url(
        r"^person/(?P<person_id>\d+)/revert$",
        views.RevertPersonView.as_view(),
        name="person-revert",
    ),
    url(
        r"^person/(?P<person_id>\d+)/merge_conflict/(?P<other_person_id>\d+)/not_standing/$",
        views.CorrectNotStandingMergeView.as_view(),
        name="person-merge-correct-not-standing",
    ),
    url(
        r"^person/(?P<person_id>\d+)/merge$",
        views.MergePeopleView.as_view(),
        name="person-merge",
    ),
    url(
        r"^person/(?P<person_id>\d+)/other-names$",
        views.PersonOtherNamesView.as_view(),
        name="person-other-names",
    ),
    url(
        r"^person/(?P<person_id>\d+)/other-names/create$",
        views.PersonOtherNameCreateView.as_view(),
        name="person-other-name-create",
    ),
    url(
        r"^person/(?P<person_id>\d+)/other-name/(?P<pk>\d+)/delete$",
        views.PersonOtherNameDeleteView.as_view(),
        name="person-other-name-delete",
    ),
    url(
        r"^person/(?P<person_id>\d+)/other-name/(?P<pk>\d+)/update/?$",
        views.PersonOtherNameUpdateView.as_view(),
        name="person-other-name-update",
    ),
    url(
        r"^person/(?P<person_id>\d+)/update/?$",
        views.UpdatePersonView.as_view(),
        name="person-update",
    ),
    url(
        r"^person/create/select_election$",
        views.NewPersonSelectElectionView.as_view(),
        name="person-create-select-election",
    ),
    url(
        r"^person/(?P<person_id>\d+)(?:/(?P<ignored_slug>.*))?$",
        views.PersonView.as_view(),
        name="person-view",
    ),
]
