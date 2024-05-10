from enum import Enum
from typing import Any, Mapping, Sequence, Union
from typing import NotRequired, TypedDict

from pulumi_types import Input

class ConditionArgsDict(TypedDict):
    """
    Condition contains details for one aspect of the current state of this API Resource.
    """
    last_transition_time: Input[str]
    """
    lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.
    """
    message: Input[str]
    """
    message is a human readable message indicating details about the transition. This may be an empty string.
    """
    reason: Input[str]
    """
    reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.
    """
    status: Input[str]
    """
    status of the condition, one of True, False, Unknown.
    """
    type: Input[str]
    """
    type of condition in CamelCase or in foo.example.com/CamelCase.
    """
    observed_generation: NotRequired[Input[int]]
    """
    observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.
    """

class LabelSelectorPatchArgsDict(TypedDict):
    """
    A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.
    """
    match_expressions: NotRequired[Input[Sequence[Input['LabelSelectorRequirementPatchArgsDict']]]]
    """
    matchExpressions is a list of label selector requirements. The requirements are ANDed.
    """
    match_labels: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """

class LabelSelectorRequirementPatchArgsDict(TypedDict):
    """
    A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    """
    key: NotRequired[Input[str]]
    """
    key is the label key that the selector applies to.
    """
    operator: NotRequired[Input[str]]
    """
    operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    """
    values: NotRequired[Input[Sequence[Input[str]]]]
    """
    values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """

class LabelSelectorRequirementArgsDict(TypedDict):
    """
    A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    """
    key: Input[str]
    """
    key is the label key that the selector applies to.
    """
    operator: Input[str]
    """
    operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
    """
    values: NotRequired[Input[Sequence[Input[str]]]]
    """
    values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """

class LabelSelectorArgsDict(TypedDict):
    """
    A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.
    """
    match_expressions: NotRequired[Input[Sequence[Input['LabelSelectorRequirementArgsDict']]]]
    """
    matchExpressions is a list of label selector requirements. The requirements are ANDed.
    """
    match_labels: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
    """

class ListMetaPatchArgsDict(TypedDict):
    """
    ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}.
    """
    continue_: NotRequired[Input[str]]
    """
    continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.
    """
    remaining_item_count: NotRequired[Input[int]]
    """
    remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.
    """
    resource_version: NotRequired[Input[str]]
    """
    String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
    """
    self_link: NotRequired[Input[str]]
    """
    Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
    """

class ListMetaArgsDict(TypedDict):
    """
    ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}.
    """
    continue_: NotRequired[Input[str]]
    """
    continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.
    """
    remaining_item_count: NotRequired[Input[int]]
    """
    remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.
    """
    resource_version: NotRequired[Input[str]]
    """
    String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
    """
    self_link: NotRequired[Input[str]]
    """
    Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
    """

class ManagedFieldsEntryPatchArgsDict(TypedDict):
    """
    ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the fieldset applies to.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.
    """
    fields_type: NotRequired[Input[str]]
    """
    FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"
    """
    fields_v1: NotRequired[Any]
    """
    FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.
    """
    manager: NotRequired[Input[str]]
    """
    Manager is an identifier of the workflow managing these fields.
    """
    operation: NotRequired[Input[str]]
    """
    Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.
    """
    subresource: NotRequired[Input[str]]
    """
    Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource.
    """
    time: NotRequired[Input[str]]
    """
    Time is the timestamp of when the ManagedFields entry was added. The timestamp will also be updated if a field is added, the manager changes any of the owned fields value or removes a field. The timestamp does not update when a field is removed from the entry because another manager took it over.
    """

class ManagedFieldsEntryArgsDict(TypedDict):
    """
    ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the fieldset applies to.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.
    """
    fields_type: NotRequired[Input[str]]
    """
    FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"
    """
    fields_v1: NotRequired[Any]
    """
    FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.
    """
    manager: NotRequired[Input[str]]
    """
    Manager is an identifier of the workflow managing these fields.
    """
    operation: NotRequired[Input[str]]
    """
    Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.
    """
    subresource: NotRequired[Input[str]]
    """
    Subresource is the name of the subresource used to update that object, or empty string if the object was updated through the main resource. The value of this field is used to distinguish between managers, even if they share the same name. For example, a status update will be distinct from a regular update using the same manager name. Note that the APIVersion field is not related to the Subresource field and it always corresponds to the version of the main resource.
    """
    time: NotRequired[Input[str]]
    """
    Time is the timestamp of when the ManagedFields entry was added. The timestamp will also be updated if a field is added, the manager changes any of the owned fields value or removes a field. The timestamp does not update when a field is removed from the entry because another manager took it over.
    """

class ObjectMetaPatchArgsDict(TypedDict):
    """
    ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.
    """
    annotations: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations
    """
    cluster_name: NotRequired[Input[str]]
    """
    The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.
    """
    creation_timestamp: NotRequired[Input[str]]
    """
    CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

    Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    deletion_grace_period_seconds: NotRequired[Input[int]]
    """
    Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.
    """
    deletion_timestamp: NotRequired[Input[str]]
    """
    DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

    Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    finalizers: NotRequired[Input[Sequence[Input[str]]]]
    """
    Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.
    """
    generate_name: NotRequired[Input[str]]
    """
    GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

    If this field is specified and the generated name exists, the server will return a 409.

    Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency
    """
    generation: NotRequired[Input[int]]
    """
    A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.
    """
    labels: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels
    """
    managed_fields: NotRequired[Input[Sequence[Input['ManagedFieldsEntryPatchArgsDict']]]]
    """
    ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.
    """
    name: NotRequired[Input[str]]
    """
    Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names
    """
    namespace: NotRequired[Input[str]]
    """
    Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

    Must be a DNS_LABEL. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces
    """
    owner_references: NotRequired[Input[Sequence[Input['OwnerReferencePatchArgsDict']]]]
    """
    List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.
    """
    resource_version: NotRequired[Input[str]]
    """
    An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

    Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
    """
    self_link: NotRequired[Input[str]]
    """
    Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
    """
    uid: NotRequired[Input[str]]
    """
    UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

    Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
    """

class ObjectMetaArgsDict(TypedDict):
    """
    ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.
    """
    annotations: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations
    """
    cluster_name: NotRequired[Input[str]]
    """
    The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.
    """
    creation_timestamp: NotRequired[Input[str]]
    """
    CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

    Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    deletion_grace_period_seconds: NotRequired[Input[int]]
    """
    Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.
    """
    deletion_timestamp: NotRequired[Input[str]]
    """
    DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

    Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    finalizers: NotRequired[Input[Sequence[Input[str]]]]
    """
    Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.
    """
    generate_name: NotRequired[Input[str]]
    """
    GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

    If this field is specified and the generated name exists, the server will return a 409.

    Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency
    """
    generation: NotRequired[Input[int]]
    """
    A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.
    """
    labels: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels
    """
    managed_fields: NotRequired[Input[Sequence[Input['ManagedFieldsEntryArgsDict']]]]
    """
    ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.
    """
    name: NotRequired[Input[str]]
    """
    Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names
    """
    namespace: NotRequired[Input[str]]
    """
    Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

    Must be a DNS_LABEL. Cannot be updated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces
    """
    owner_references: NotRequired[Input[Sequence[Input['OwnerReferenceArgsDict']]]]
    """
    List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.
    """
    resource_version: NotRequired[Input[str]]
    """
    An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

    Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
    """
    self_link: NotRequired[Input[str]]
    """
    Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
    """
    uid: NotRequired[Input[str]]
    """
    UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

    Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
    """

class OwnerReferencePatchArgsDict(TypedDict):
    """
    OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.
    """
    api_version: NotRequired[Input[str]]
    """
    API version of the referent.
    """
    block_owner_deletion: NotRequired[Input[bool]]
    """
    If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.
    """
    controller: NotRequired[Input[bool]]
    """
    If true, this reference points to the managing controller.
    """
    kind: NotRequired[Input[str]]
    """
    Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names
    """
    uid: NotRequired[Input[str]]
    """
    UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
    """

class OwnerReferenceArgsDict(TypedDict):
    """
    OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.
    """
    api_version: Input[str]
    """
    API version of the referent.
    """
    kind: Input[str]
    """
    Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    name: Input[str]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names
    """
    uid: Input[str]
    """
    UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
    """
    block_owner_deletion: NotRequired[Input[bool]]
    """
    If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.
    """
    controller: NotRequired[Input[bool]]
    """
    If true, this reference points to the managing controller.
    """

class StatusCausePatchArgsDict(TypedDict):
    """
    StatusCause provides more information about an api.Status failure, including cases when multiple errors are encountered.
    """
    field: NotRequired[Input[str]]
    """
    The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.

    Examples:
      "name" - the field "name" on the current resource
      "items[0].name" - the field "name" on the first array entry in "items"
    """
    message: NotRequired[Input[str]]
    """
    A human-readable description of the cause of the error.  This field may be presented as-is to a reader.
    """
    reason: NotRequired[Input[str]]
    """
    A machine-readable description of the cause of the error. If this value is empty there is no information available.
    """

class StatusCauseArgsDict(TypedDict):
    """
    StatusCause provides more information about an api.Status failure, including cases when multiple errors are encountered.
    """
    field: NotRequired[Input[str]]
    """
    The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.

    Examples:
      "name" - the field "name" on the current resource
      "items[0].name" - the field "name" on the first array entry in "items"
    """
    message: NotRequired[Input[str]]
    """
    A human-readable description of the cause of the error.  This field may be presented as-is to a reader.
    """
    reason: NotRequired[Input[str]]
    """
    A machine-readable description of the cause of the error. If this value is empty there is no information available.
    """

class StatusDetailsPatchArgsDict(TypedDict):
    """
    StatusDetails is a set of additional properties that MAY be set by the server to provide additional information about a response. The Reason field of a Status object defines what attributes will be set. Clients must ignore fields that do not match the defined type of each attribute, and should assume that any attribute may be empty, invalid, or under defined.
    """
    causes: NotRequired[Input[Sequence[Input['StatusCausePatchArgsDict']]]]
    """
    The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.
    """
    group: NotRequired[Input[str]]
    """
    The group attribute of the resource associated with the status StatusReason.
    """
    kind: NotRequired[Input[str]]
    """
    The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    name: NotRequired[Input[str]]
    """
    The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).
    """
    retry_after_seconds: NotRequired[Input[int]]
    """
    If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.
    """
    uid: NotRequired[Input[str]]
    """
    UID of the resource. (when there is a single resource which can be described). More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
    """

class StatusDetailsArgsDict(TypedDict):
    """
    StatusDetails is a set of additional properties that MAY be set by the server to provide additional information about a response. The Reason field of a Status object defines what attributes will be set. Clients must ignore fields that do not match the defined type of each attribute, and should assume that any attribute may be empty, invalid, or under defined.
    """
    causes: NotRequired[Input[Sequence[Input['StatusCauseArgsDict']]]]
    """
    The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.
    """
    group: NotRequired[Input[str]]
    """
    The group attribute of the resource associated with the status StatusReason.
    """
    kind: NotRequired[Input[str]]
    """
    The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    name: NotRequired[Input[str]]
    """
    The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).
    """
    retry_after_seconds: NotRequired[Input[int]]
    """
    If specified, the time in seconds before the operation should be retried. Some errors may indicate the client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action.
    """
    uid: NotRequired[Input[str]]
    """
    UID of the resource. (when there is a single resource which can be described). More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids
    """



class AWSElasticBlockStoreVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Persistent Disk resource in AWS.

    An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    partition: NotRequired[Input[int]]
    """
    partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    volume_id: NotRequired[Input[str]]
    """
    volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """

class AWSElasticBlockStoreVolumeSourceArgsDict(TypedDict):
    """
    Represents a Persistent Disk resource in AWS.

    An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.
    """
    volume_id: Input[str]
    """
    volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    partition: NotRequired[Input[int]]
    """
    partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """

class AffinityPatchArgsDict(TypedDict):
    """
    Affinity is a group of affinity scheduling rules.
    """
    node_affinity: NotRequired[Input['NodeAffinityPatchArgsDict']]
    """
    Describes node affinity scheduling rules for the pod.
    """
    pod_affinity: NotRequired[Input['PodAffinityPatchArgsDict']]
    """
    Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    """
    pod_anti_affinity: NotRequired[Input['PodAntiAffinityPatchArgsDict']]
    """
    Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    """

class AffinityArgsDict(TypedDict):
    """
    Affinity is a group of affinity scheduling rules.
    """
    node_affinity: NotRequired[Input['NodeAffinityArgsDict']]
    """
    Describes node affinity scheduling rules for the pod.
    """
    pod_affinity: NotRequired[Input['PodAffinityArgsDict']]
    """
    Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    """
    pod_anti_affinity: NotRequired[Input['PodAntiAffinityArgsDict']]
    """
    Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).
    """

class AppArmorProfilePatchArgsDict(TypedDict):
    """
    AppArmorProfile defines a pod or container's AppArmor settings.
    """
    localhost_profile: NotRequired[Input[str]]
    """
    localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".
    """
    type: NotRequired[Input[str]]
    """
    type indicates which kind of AppArmor profile will be applied. Valid options are:
      Localhost - a profile pre-loaded on the node.
      RuntimeDefault - the container runtime's default profile.
      Unconfined - no AppArmor enforcement.
    """

class AppArmorProfileArgsDict(TypedDict):
    """
    AppArmorProfile defines a pod or container's AppArmor settings.
    """
    type: Input[str]
    """
    type indicates which kind of AppArmor profile will be applied. Valid options are:
      Localhost - a profile pre-loaded on the node.
      RuntimeDefault - the container runtime's default profile.
      Unconfined - no AppArmor enforcement.
    """
    localhost_profile: NotRequired[Input[str]]
    """
    localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".
    """

class AttachedVolumeArgsDict(TypedDict):
    """
    AttachedVolume describes a volume attached to a node
    """
    device_path: Input[str]
    """
    DevicePath represents the device path where the volume should be available
    """
    name: Input[str]
    """
    Name of the attached volume
    """

class AzureDiskVolumeSourcePatchArgsDict(TypedDict):
    """
    AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    """
    caching_mode: NotRequired[Input[str]]
    """
    cachingMode is the Host Caching mode: None, Read Only, Read Write.
    """
    disk_name: NotRequired[Input[str]]
    """
    diskName is the Name of the data disk in the blob storage
    """
    disk_uri: NotRequired[Input[str]]
    """
    diskURI is the URI of data disk in the blob storage
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    kind: NotRequired[Input[str]]
    """
    kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """

class AzureDiskVolumeSourceArgsDict(TypedDict):
    """
    AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    """
    disk_name: Input[str]
    """
    diskName is the Name of the data disk in the blob storage
    """
    disk_uri: Input[str]
    """
    diskURI is the URI of data disk in the blob storage
    """
    caching_mode: NotRequired[Input[str]]
    """
    cachingMode is the Host Caching mode: None, Read Only, Read Write.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    kind: NotRequired[Input[str]]
    """
    kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """

class AzureFilePersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_name: NotRequired[Input[str]]
    """
    secretName is the name of secret that contains Azure Storage Account Name and Key
    """
    secret_namespace: NotRequired[Input[str]]
    """
    secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod
    """
    share_name: NotRequired[Input[str]]
    """
    shareName is the azure Share Name
    """

class AzureFilePersistentVolumeSourceArgsDict(TypedDict):
    """
    AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    """
    secret_name: Input[str]
    """
    secretName is the name of secret that contains Azure Storage Account Name and Key
    """
    share_name: Input[str]
    """
    shareName is the azure Share Name
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_namespace: NotRequired[Input[str]]
    """
    secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod
    """

class AzureFileVolumeSourcePatchArgsDict(TypedDict):
    """
    AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_name: NotRequired[Input[str]]
    """
    secretName is the  name of secret that contains Azure Storage Account Name and Key
    """
    share_name: NotRequired[Input[str]]
    """
    shareName is the azure share Name
    """

class AzureFileVolumeSourceArgsDict(TypedDict):
    """
    AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
    """
    secret_name: Input[str]
    """
    secretName is the  name of secret that contains Azure Storage Account Name and Key
    """
    share_name: Input[str]
    """
    shareName is the azure share Name
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """

class CSIPersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents storage that is managed by an external CSI volume driver (Beta feature)
    """
    controller_expand_secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    controller_publish_secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    driver: NotRequired[Input[str]]
    """
    driver is the name of the driver to use for this volume. Required.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".
    """
    node_expand_secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    node_publish_secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    node_stage_secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).
    """
    volume_attributes: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    volumeAttributes of the volume to publish.
    """
    volume_handle: NotRequired[Input[str]]
    """
    volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.
    """

class CSIPersistentVolumeSourceArgsDict(TypedDict):
    """
    Represents storage that is managed by an external CSI volume driver (Beta feature)
    """
    driver: Input[str]
    """
    driver is the name of the driver to use for this volume. Required.
    """
    volume_handle: Input[str]
    """
    volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.
    """
    controller_expand_secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    controller_publish_secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".
    """
    node_expand_secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    node_publish_secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    node_stage_secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).
    """
    volume_attributes: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    volumeAttributes of the volume to publish.
    """

class CSIVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a source location of a volume to mount, managed by an external CSI driver
    """
    driver: NotRequired[Input[str]]
    """
    driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.
    """
    node_publish_secret_ref: NotRequired[Input['LocalObjectReferencePatchArgsDict']]
    """
    nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly specifies a read-only configuration for the volume. Defaults to false (read/write).
    """
    volume_attributes: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.
    """

class CSIVolumeSourceArgsDict(TypedDict):
    """
    Represents a source location of a volume to mount, managed by an external CSI driver
    """
    driver: Input[str]
    """
    driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.
    """
    node_publish_secret_ref: NotRequired[Input['LocalObjectReferenceArgsDict']]
    """
    nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly specifies a read-only configuration for the volume. Defaults to false (read/write).
    """
    volume_attributes: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.
    """

class CapabilitiesPatchArgsDict(TypedDict):
    """
    Adds and removes POSIX capabilities from running containers.
    """
    add: NotRequired[Input[Sequence[Input[str]]]]
    """
    Added capabilities
    """
    drop: NotRequired[Input[Sequence[Input[str]]]]
    """
    Removed capabilities
    """

class CapabilitiesArgsDict(TypedDict):
    """
    Adds and removes POSIX capabilities from running containers.
    """
    add: NotRequired[Input[Sequence[Input[str]]]]
    """
    Added capabilities
    """
    drop: NotRequired[Input[Sequence[Input[str]]]]
    """
    Removed capabilities
    """

class CephFSPersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.
    """
    monitors: NotRequired[Input[Sequence[Input[str]]]]
    """
    monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    path: NotRequired[Input[str]]
    """
    path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    secret_file: NotRequired[Input[str]]
    """
    secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    user: NotRequired[Input[str]]
    """
    user is Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """

class CephFSPersistentVolumeSourceArgsDict(TypedDict):
    """
    Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.
    """
    monitors: Input[Sequence[Input[str]]]
    """
    monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    path: NotRequired[Input[str]]
    """
    path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    secret_file: NotRequired[Input[str]]
    """
    secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    user: NotRequired[Input[str]]
    """
    user is Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """

class CephFSVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.
    """
    monitors: NotRequired[Input[Sequence[Input[str]]]]
    """
    monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    path: NotRequired[Input[str]]
    """
    path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    secret_file: NotRequired[Input[str]]
    """
    secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    secret_ref: NotRequired[Input['LocalObjectReferencePatchArgsDict']]
    """
    secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    user: NotRequired[Input[str]]
    """
    user is optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """

class CephFSVolumeSourceArgsDict(TypedDict):
    """
    Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.
    """
    monitors: Input[Sequence[Input[str]]]
    """
    monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    path: NotRequired[Input[str]]
    """
    path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    secret_file: NotRequired[Input[str]]
    """
    secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    secret_ref: NotRequired[Input['LocalObjectReferenceArgsDict']]
    """
    secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """
    user: NotRequired[Input[str]]
    """
    user is optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it
    """

class CinderPersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    secretRef is Optional: points to a secret object containing parameters used to connect to OpenStack.
    """
    volume_id: NotRequired[Input[str]]
    """
    volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """

class CinderPersistentVolumeSourceArgsDict(TypedDict):
    """
    Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.
    """
    volume_id: Input[str]
    """
    volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    secretRef is Optional: points to a secret object containing parameters used to connect to OpenStack.
    """

class CinderVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    secret_ref: NotRequired[Input['LocalObjectReferencePatchArgsDict']]
    """
    secretRef is optional: points to a secret object containing parameters used to connect to OpenStack.
    """
    volume_id: NotRequired[Input[str]]
    """
    volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """

class CinderVolumeSourceArgsDict(TypedDict):
    """
    Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.
    """
    volume_id: Input[str]
    """
    volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    secret_ref: NotRequired[Input['LocalObjectReferenceArgsDict']]
    """
    secretRef is optional: points to a secret object containing parameters used to connect to OpenStack.
    """

class ClaimSourcePatchArgsDict(TypedDict):
    """
    ClaimSource describes a reference to a ResourceClaim.

    Exactly one of these fields should be set.  Consumers of this type must treat an empty object as if it has an unknown value.
    """
    resource_claim_name: NotRequired[Input[str]]
    """
    ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.
    """
    resource_claim_template_name: NotRequired[Input[str]]
    """
    ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.

    The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.

    This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.
    """

class ClaimSourceArgsDict(TypedDict):
    """
    ClaimSource describes a reference to a ResourceClaim.

    Exactly one of these fields should be set.  Consumers of this type must treat an empty object as if it has an unknown value.
    """
    resource_claim_name: NotRequired[Input[str]]
    """
    ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.
    """
    resource_claim_template_name: NotRequired[Input[str]]
    """
    ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.

    The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.

    This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.
    """

class ClientIPConfigPatchArgsDict(TypedDict):
    """
    ClientIPConfig represents the configurations of Client IP based session affinity.
    """
    timeout_seconds: NotRequired[Input[int]]
    """
    timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3 hours).
    """

class ClientIPConfigArgsDict(TypedDict):
    """
    ClientIPConfig represents the configurations of Client IP based session affinity.
    """
    timeout_seconds: NotRequired[Input[int]]
    """
    timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3 hours).
    """

class ClusterTrustBundleProjectionPatchArgsDict(TypedDict):
    """
    ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem.
    """
    label_selector: NotRequired[Input['LabelSelectorPatchArgsDict']]
    """
    Select all ClusterTrustBundles that match this label selector.  Only has effect if signerName is set.  Mutually-exclusive with name.  If unset, interpreted as "match nothing".  If set but empty, interpreted as "match everything".
    """
    name: NotRequired[Input[str]]
    """
    Select a single ClusterTrustBundle by object name.  Mutually-exclusive with signerName and labelSelector.
    """
    optional: NotRequired[Input[bool]]
    """
    If true, don't block pod startup if the referenced ClusterTrustBundle(s) aren't available.  If using name, then the named ClusterTrustBundle is allowed not to exist.  If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles.
    """
    path: NotRequired[Input[str]]
    """
    Relative path from the volume root to write the bundle.
    """
    signer_name: NotRequired[Input[str]]
    """
    Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name.  The contents of all selected ClusterTrustBundles will be unified and deduplicated.
    """

class ClusterTrustBundleProjectionArgsDict(TypedDict):
    """
    ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem.
    """
    path: Input[str]
    """
    Relative path from the volume root to write the bundle.
    """
    label_selector: NotRequired[Input['LabelSelectorArgsDict']]
    """
    Select all ClusterTrustBundles that match this label selector.  Only has effect if signerName is set.  Mutually-exclusive with name.  If unset, interpreted as "match nothing".  If set but empty, interpreted as "match everything".
    """
    name: NotRequired[Input[str]]
    """
    Select a single ClusterTrustBundle by object name.  Mutually-exclusive with signerName and labelSelector.
    """
    optional: NotRequired[Input[bool]]
    """
    If true, don't block pod startup if the referenced ClusterTrustBundle(s) aren't available.  If using name, then the named ClusterTrustBundle is allowed not to exist.  If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles.
    """
    signer_name: NotRequired[Input[str]]
    """
    Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name.  The contents of all selected ClusterTrustBundles will be unified and deduplicated.
    """

class ConfigMapEnvSourcePatchArgsDict(TypedDict):
    """
    ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

    The contents of the target ConfigMap's Data field will represent the key-value pairs as environment variables.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    Specify whether the ConfigMap must be defined
    """

class ConfigMapEnvSourceArgsDict(TypedDict):
    """
    ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

    The contents of the target ConfigMap's Data field will represent the key-value pairs as environment variables.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    Specify whether the ConfigMap must be defined
    """

class ConfigMapKeySelectorPatchArgsDict(TypedDict):
    """
    Selects a key from a ConfigMap.
    """
    key: NotRequired[Input[str]]
    """
    The key to select.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    Specify whether the ConfigMap or its key must be defined
    """

class ConfigMapKeySelectorArgsDict(TypedDict):
    """
    Selects a key from a ConfigMap.
    """
    key: Input[str]
    """
    The key to select.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    Specify whether the ConfigMap or its key must be defined
    """

class ConfigMapNodeConfigSourcePatchArgsDict(TypedDict):
    """
    ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration
    """
    kubelet_config_key: NotRequired[Input[str]]
    """
    KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.
    """
    name: NotRequired[Input[str]]
    """
    Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.
    """
    namespace: NotRequired[Input[str]]
    """
    Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.
    """
    resource_version: NotRequired[Input[str]]
    """
    ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
    """
    uid: NotRequired[Input[str]]
    """
    UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
    """

class ConfigMapNodeConfigSourceArgsDict(TypedDict):
    """
    ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration
    """
    kubelet_config_key: Input[str]
    """
    KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.
    """
    name: Input[str]
    """
    Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.
    """
    namespace: Input[str]
    """
    Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.
    """
    resource_version: NotRequired[Input[str]]
    """
    ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
    """
    uid: NotRequired[Input[str]]
    """
    UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.
    """

class ConfigMapProjectionPatchArgsDict(TypedDict):
    """
    Adapts a ConfigMap into a projected volume.

    The contents of the target ConfigMap's Data field will be presented in a projected volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. Note that this is identical to a configmap volume source without the default mode.
    """
    items: NotRequired[Input[Sequence[Input['KeyToPathPatchArgsDict']]]]
    """
    items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    optional specify whether the ConfigMap or its keys must be defined
    """

class ConfigMapProjectionArgsDict(TypedDict):
    """
    Adapts a ConfigMap into a projected volume.

    The contents of the target ConfigMap's Data field will be presented in a projected volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. Note that this is identical to a configmap volume source without the default mode.
    """
    items: NotRequired[Input[Sequence[Input['KeyToPathArgsDict']]]]
    """
    items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    optional specify whether the ConfigMap or its keys must be defined
    """

class ConfigMapVolumeSourcePatchArgsDict(TypedDict):
    """
    Adapts a ConfigMap into a volume.

    The contents of the target ConfigMap's Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.
    """
    default_mode: NotRequired[Input[int]]
    """
    defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    items: NotRequired[Input[Sequence[Input['KeyToPathPatchArgsDict']]]]
    """
    items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    optional specify whether the ConfigMap or its keys must be defined
    """

class ConfigMapVolumeSourceArgsDict(TypedDict):
    """
    Adapts a ConfigMap into a volume.

    The contents of the target ConfigMap's Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.
    """
    default_mode: NotRequired[Input[int]]
    """
    defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    items: NotRequired[Input[Sequence[Input['KeyToPathArgsDict']]]]
    """
    items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    optional specify whether the ConfigMap or its keys must be defined
    """

class ConfigMapArgsDict(TypedDict):
    """
    ConfigMap holds configuration data for pods to consume.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    binary_data: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet.
    """
    data: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process.
    """
    immutable: NotRequired[Input[bool]]
    """
    Immutable, if set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil.
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """

class ContainerImageArgsDict(TypedDict):
    """
    Describe a container image
    """
    names: Input[Sequence[Input[str]]]
    """
    Names by which this image is known. e.g. ["kubernetes.example/hyperkube:v1.0.7", "cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7"]
    """
    size_bytes: NotRequired[Input[int]]
    """
    The size of the image in bytes.
    """

class ContainerPatchArgsDict(TypedDict):
    """
    A single application container that you want to run within a pod.
    """
    args: NotRequired[Input[Sequence[Input[str]]]]
    """
    Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    """
    command: NotRequired[Input[Sequence[Input[str]]]]
    """
    Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    """
    env: NotRequired[Input[Sequence[Input['EnvVarPatchArgsDict']]]]
    """
    List of environment variables to set in the container. Cannot be updated.
    """
    env_from: NotRequired[Input[Sequence[Input['EnvFromSourcePatchArgsDict']]]]
    """
    List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.
    """
    image: NotRequired[Input[str]]
    """
    Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.
    """
    image_pull_policy: NotRequired[Input[str]]
    """
    Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images
    """
    lifecycle: NotRequired[Input['LifecyclePatchArgsDict']]
    """
    Actions that the management system should take in response to container lifecycle events. Cannot be updated.
    """
    liveness_probe: NotRequired[Input['ProbePatchArgsDict']]
    """
    Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    name: NotRequired[Input[str]]
    """
    Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.
    """
    ports: NotRequired[Input[Sequence[Input['ContainerPortPatchArgsDict']]]]
    """
    List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated.
    """
    readiness_probe: NotRequired[Input['ProbePatchArgsDict']]
    """
    Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    resize_policy: NotRequired[Input[Sequence[Input['ContainerResizePolicyPatchArgsDict']]]]
    """
    Resources resize policy for the container.
    """
    resources: NotRequired[Input['ResourceRequirementsPatchArgsDict']]
    """
    Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """
    restart_policy: NotRequired[Input[str]]
    """
    RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod's restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.
    """
    security_context: NotRequired[Input['SecurityContextPatchArgsDict']]
    """
    SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
    """
    startup_probe: NotRequired[Input['ProbePatchArgsDict']]
    """
    StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    stdin: NotRequired[Input[bool]]
    """
    Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.
    """
    stdin_once: NotRequired[Input[bool]]
    """
    Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false
    """
    termination_message_path: NotRequired[Input[str]]
    """
    Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.
    """
    termination_message_policy: NotRequired[Input[str]]
    """
    Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.
    """
    tty: NotRequired[Input[bool]]
    """
    Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.
    """
    volume_devices: NotRequired[Input[Sequence[Input['VolumeDevicePatchArgsDict']]]]
    """
    volumeDevices is the list of block devices to be used by the container.
    """
    volume_mounts: NotRequired[Input[Sequence[Input['VolumeMountPatchArgsDict']]]]
    """
    Pod volumes to mount into the container's filesystem. Cannot be updated.
    """
    working_dir: NotRequired[Input[str]]
    """
    Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.
    """

class ContainerPortPatchArgsDict(TypedDict):
    """
    ContainerPort represents a network port in a single container.
    """
    container_port: NotRequired[Input[int]]
    """
    Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.
    """
    host_ip: NotRequired[Input[str]]
    """
    What host IP to bind the external port to.
    """
    host_port: NotRequired[Input[int]]
    """
    Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.
    """
    name: NotRequired[Input[str]]
    """
    If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.
    """
    protocol: NotRequired[Input[str]]
    """
    Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".
    """

class ContainerPortArgsDict(TypedDict):
    """
    ContainerPort represents a network port in a single container.
    """
    container_port: Input[int]
    """
    Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.
    """
    host_ip: NotRequired[Input[str]]
    """
    What host IP to bind the external port to.
    """
    host_port: NotRequired[Input[int]]
    """
    Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.
    """
    name: NotRequired[Input[str]]
    """
    If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.
    """
    protocol: NotRequired[Input[str]]
    """
    Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".
    """

class ContainerResizePolicyPatchArgsDict(TypedDict):
    """
    ContainerResizePolicy represents resource resize policy for the container.
    """
    resource_name: NotRequired[Input[str]]
    """
    Name of the resource to which this resource resize policy applies. Supported values: cpu, memory.
    """
    restart_policy: NotRequired[Input[str]]
    """
    Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired.
    """

class ContainerResizePolicyArgsDict(TypedDict):
    """
    ContainerResizePolicy represents resource resize policy for the container.
    """
    resource_name: Input[str]
    """
    Name of the resource to which this resource resize policy applies. Supported values: cpu, memory.
    """
    restart_policy: Input[str]
    """
    Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired.
    """

class ContainerStateRunningArgsDict(TypedDict):
    """
    ContainerStateRunning is a running state of a container.
    """
    started_at: NotRequired[Input[str]]
    """
    Time at which the container was last (re-)started
    """

class ContainerStateTerminatedArgsDict(TypedDict):
    """
    ContainerStateTerminated is a terminated state of a container.
    """
    exit_code: Input[int]
    """
    Exit status from the last termination of the container
    """
    container_id: NotRequired[Input[str]]
    """
    Container's ID in the format '<type>://<container_id>'
    """
    finished_at: NotRequired[Input[str]]
    """
    Time at which the container last terminated
    """
    message: NotRequired[Input[str]]
    """
    Message regarding the last termination of the container
    """
    reason: NotRequired[Input[str]]
    """
    (brief) reason from the last termination of the container
    """
    signal: NotRequired[Input[int]]
    """
    Signal from the last termination of the container
    """
    started_at: NotRequired[Input[str]]
    """
    Time at which previous execution of the container started
    """

class ContainerStateWaitingArgsDict(TypedDict):
    """
    ContainerStateWaiting is a waiting state of a container.
    """
    message: NotRequired[Input[str]]
    """
    Message regarding why the container is not yet running.
    """
    reason: NotRequired[Input[str]]
    """
    (brief) reason the container is not yet running.
    """

class ContainerStateArgsDict(TypedDict):
    """
    ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.
    """
    running: NotRequired[Input['ContainerStateRunningArgsDict']]
    """
    Details about a running container
    """
    terminated: NotRequired[Input['ContainerStateTerminatedArgsDict']]
    """
    Details about a terminated container
    """
    waiting: NotRequired[Input['ContainerStateWaitingArgsDict']]
    """
    Details about a waiting container
    """

class ContainerStatusArgsDict(TypedDict):
    """
    ContainerStatus contains details for the current status of this container.
    """
    image: Input[str]
    """
    Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images.
    """
    image_id: Input[str]
    """
    ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime.
    """
    name: Input[str]
    """
    Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated.
    """
    ready: Input[bool]
    """
    Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).

    The value is typically used to determine whether a container is ready to accept traffic.
    """
    restart_count: Input[int]
    """
    RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative.
    """
    allocated_resources: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize.
    """
    container_id: NotRequired[Input[str]]
    """
    ContainerID is the ID of the container in the format '<type>://<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example "containerd").
    """
    last_state: NotRequired[Input['ContainerStateArgsDict']]
    """
    LastTerminationState holds the last termination state of the container to help debug container crashes and restarts. This field is not populated if the container is still running and RestartCount is 0.
    """
    resources: NotRequired[Input['ResourceRequirementsArgsDict']]
    """
    Resources represents the compute resource requests and limits that have been successfully enacted on the running container after it has been started or has been successfully resized.
    """
    started: NotRequired[Input[bool]]
    """
    Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false.
    """
    state: NotRequired[Input['ContainerStateArgsDict']]
    """
    State holds details about the container's current condition.
    """
    volume_mounts: NotRequired[Input[Sequence[Input['VolumeMountStatusArgsDict']]]]
    """
    Status of volume mounts.
    """

class ContainerArgsDict(TypedDict):
    """
    A single application container that you want to run within a pod.
    """
    name: Input[str]
    """
    Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.
    """
    args: NotRequired[Input[Sequence[Input[str]]]]
    """
    Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    """
    command: NotRequired[Input[Sequence[Input[str]]]]
    """
    Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    """
    env: NotRequired[Input[Sequence[Input['EnvVarArgsDict']]]]
    """
    List of environment variables to set in the container. Cannot be updated.
    """
    env_from: NotRequired[Input[Sequence[Input['EnvFromSourceArgsDict']]]]
    """
    List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.
    """
    image: NotRequired[Input[str]]
    """
    Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.
    """
    image_pull_policy: NotRequired[Input[str]]
    """
    Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images
    """
    lifecycle: NotRequired[Input['LifecycleArgsDict']]
    """
    Actions that the management system should take in response to container lifecycle events. Cannot be updated.
    """
    liveness_probe: NotRequired[Input['ProbeArgsDict']]
    """
    Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    ports: NotRequired[Input[Sequence[Input['ContainerPortArgsDict']]]]
    """
    List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated.
    """
    readiness_probe: NotRequired[Input['ProbeArgsDict']]
    """
    Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    resize_policy: NotRequired[Input[Sequence[Input['ContainerResizePolicyArgsDict']]]]
    """
    Resources resize policy for the container.
    """
    resources: NotRequired[Input['ResourceRequirementsArgsDict']]
    """
    Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """
    restart_policy: NotRequired[Input[str]]
    """
    RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod's restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.
    """
    security_context: NotRequired[Input['SecurityContextArgsDict']]
    """
    SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
    """
    startup_probe: NotRequired[Input['ProbeArgsDict']]
    """
    StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    stdin: NotRequired[Input[bool]]
    """
    Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.
    """
    stdin_once: NotRequired[Input[bool]]
    """
    Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false
    """
    termination_message_path: NotRequired[Input[str]]
    """
    Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.
    """
    termination_message_policy: NotRequired[Input[str]]
    """
    Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.
    """
    tty: NotRequired[Input[bool]]
    """
    Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.
    """
    volume_devices: NotRequired[Input[Sequence[Input['VolumeDeviceArgsDict']]]]
    """
    volumeDevices is the list of block devices to be used by the container.
    """
    volume_mounts: NotRequired[Input[Sequence[Input['VolumeMountArgsDict']]]]
    """
    Pod volumes to mount into the container's filesystem. Cannot be updated.
    """
    working_dir: NotRequired[Input[str]]
    """
    Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.
    """

class DaemonEndpointArgsDict(TypedDict):
    """
    DaemonEndpoint contains information about a single Daemon endpoint.
    """
    port: Input[int]
    """
    Port number of the given endpoint.
    """

class DownwardAPIProjectionPatchArgsDict(TypedDict):
    """
    Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode.
    """
    items: NotRequired[Input[Sequence[Input['DownwardAPIVolumeFilePatchArgsDict']]]]
    """
    Items is a list of DownwardAPIVolume file
    """

class DownwardAPIProjectionArgsDict(TypedDict):
    """
    Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode.
    """
    items: NotRequired[Input[Sequence[Input['DownwardAPIVolumeFileArgsDict']]]]
    """
    Items is a list of DownwardAPIVolume file
    """

class DownwardAPIVolumeFilePatchArgsDict(TypedDict):
    """
    DownwardAPIVolumeFile represents information to create the file containing the pod field
    """
    field_ref: NotRequired[Input['ObjectFieldSelectorPatchArgsDict']]
    """
    Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.
    """
    mode: NotRequired[Input[int]]
    """
    Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    path: NotRequired[Input[str]]
    """
    Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'
    """
    resource_field_ref: NotRequired[Input['ResourceFieldSelectorPatchArgsDict']]
    """
    Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """

class DownwardAPIVolumeFileArgsDict(TypedDict):
    """
    DownwardAPIVolumeFile represents information to create the file containing the pod field
    """
    path: Input[str]
    """
    Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'
    """
    field_ref: NotRequired[Input['ObjectFieldSelectorArgsDict']]
    """
    Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.
    """
    mode: NotRequired[Input[int]]
    """
    Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    resource_field_ref: NotRequired[Input['ResourceFieldSelectorArgsDict']]
    """
    Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.
    """

class DownwardAPIVolumeSourcePatchArgsDict(TypedDict):
    """
    DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling.
    """
    default_mode: NotRequired[Input[int]]
    """
    Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    items: NotRequired[Input[Sequence[Input['DownwardAPIVolumeFilePatchArgsDict']]]]
    """
    Items is a list of downward API volume file
    """

class DownwardAPIVolumeSourceArgsDict(TypedDict):
    """
    DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling.
    """
    default_mode: NotRequired[Input[int]]
    """
    Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    items: NotRequired[Input[Sequence[Input['DownwardAPIVolumeFileArgsDict']]]]
    """
    Items is a list of downward API volume file
    """

class EmptyDirVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling.
    """
    medium: NotRequired[Input[str]]
    """
    medium represents what type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    """
    size_limit: NotRequired[Input[str]]
    """
    sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    """

class EmptyDirVolumeSourceArgsDict(TypedDict):
    """
    Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling.
    """
    medium: NotRequired[Input[str]]
    """
    medium represents what type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    """
    size_limit: NotRequired[Input[str]]
    """
    sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    """

class EndpointAddressPatchArgsDict(TypedDict):
    """
    EndpointAddress is a tuple that describes single IP address.
    """
    hostname: NotRequired[Input[str]]
    """
    The Hostname of this endpoint
    """
    ip: NotRequired[Input[str]]
    """
    The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16).
    """
    node_name: NotRequired[Input[str]]
    """
    Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.
    """
    target_ref: NotRequired[Input['ObjectReferencePatchArgsDict']]
    """
    Reference to object providing the endpoint.
    """

class EndpointAddressArgsDict(TypedDict):
    """
    EndpointAddress is a tuple that describes single IP address.
    """
    ip: Input[str]
    """
    The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16).
    """
    hostname: NotRequired[Input[str]]
    """
    The Hostname of this endpoint
    """
    node_name: NotRequired[Input[str]]
    """
    Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.
    """
    target_ref: NotRequired[Input['ObjectReferenceArgsDict']]
    """
    Reference to object providing the endpoint.
    """

class EndpointPortPatchArgsDict(TypedDict):
    """
    EndpointPort is a tuple that describes a single port.
    """
    app_protocol: NotRequired[Input[str]]
    """
    The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:

    * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).

    * Kubernetes-defined prefixed names:
      * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
      * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
      * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455

    * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.
    """
    name: NotRequired[Input[str]]
    """
    The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined.
    """
    port: NotRequired[Input[int]]
    """
    The port number of the endpoint.
    """
    protocol: NotRequired[Input[str]]
    """
    The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
    """

class EndpointPortArgsDict(TypedDict):
    """
    EndpointPort is a tuple that describes a single port.
    """
    port: Input[int]
    """
    The port number of the endpoint.
    """
    app_protocol: NotRequired[Input[str]]
    """
    The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:

    * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).

    * Kubernetes-defined prefixed names:
      * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
      * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
      * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455

    * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.
    """
    name: NotRequired[Input[str]]
    """
    The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined.
    """
    protocol: NotRequired[Input[str]]
    """
    The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
    """

class EndpointSubsetPatchArgsDict(TypedDict):
    """
    EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:

    	{
    	  Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
    	  Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
    	}

    The resulting set of endpoints can be viewed as:

    	a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
    	b: [ 10.10.1.1:309, 10.10.2.2:309 ]
    """
    addresses: NotRequired[Input[Sequence[Input['EndpointAddressPatchArgsDict']]]]
    """
    IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.
    """
    not_ready_addresses: NotRequired[Input[Sequence[Input['EndpointAddressPatchArgsDict']]]]
    """
    IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.
    """
    ports: NotRequired[Input[Sequence[Input['EndpointPortPatchArgsDict']]]]
    """
    Port numbers available on the related IP addresses.
    """

class EndpointSubsetArgsDict(TypedDict):
    """
    EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:

    	{
    	  Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
    	  Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
    	}

    The resulting set of endpoints can be viewed as:

    	a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
    	b: [ 10.10.1.1:309, 10.10.2.2:309 ]
    """
    addresses: NotRequired[Input[Sequence[Input['EndpointAddressArgsDict']]]]
    """
    IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.
    """
    not_ready_addresses: NotRequired[Input[Sequence[Input['EndpointAddressArgsDict']]]]
    """
    IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.
    """
    ports: NotRequired[Input[Sequence[Input['EndpointPortArgsDict']]]]
    """
    Port numbers available on the related IP addresses.
    """

class EndpointsArgsDict(TypedDict):
    """
    Endpoints is a collection of endpoints that implement the actual service. Example:

    	 Name: "mysvc",
    	 Subsets: [
    	   {
    	     Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
    	     Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
    	   },
    	   {
    	     Addresses: [{"ip": "10.10.3.3"}],
    	     Ports: [{"name": "a", "port": 93}, {"name": "b", "port": 76}]
    	   },
    	]
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    subsets: NotRequired[Input[Sequence[Input['EndpointSubsetArgsDict']]]]
    """
    The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service.
    """

class EnvFromSourcePatchArgsDict(TypedDict):
    """
    EnvFromSource represents the source of a set of ConfigMaps
    """
    config_map_ref: NotRequired[Input['ConfigMapEnvSourcePatchArgsDict']]
    """
    The ConfigMap to select from
    """
    prefix: NotRequired[Input[str]]
    """
    An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.
    """
    secret_ref: NotRequired[Input['SecretEnvSourcePatchArgsDict']]
    """
    The Secret to select from
    """

class EnvFromSourceArgsDict(TypedDict):
    """
    EnvFromSource represents the source of a set of ConfigMaps
    """
    config_map_ref: NotRequired[Input['ConfigMapEnvSourceArgsDict']]
    """
    The ConfigMap to select from
    """
    prefix: NotRequired[Input[str]]
    """
    An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.
    """
    secret_ref: NotRequired[Input['SecretEnvSourceArgsDict']]
    """
    The Secret to select from
    """

class EnvVarPatchArgsDict(TypedDict):
    """
    EnvVar represents an environment variable present in a Container.
    """
    name: NotRequired[Input[str]]
    """
    Name of the environment variable. Must be a C_IDENTIFIER.
    """
    value: NotRequired[Input[str]]
    """
    Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".
    """
    value_from: NotRequired[Input['EnvVarSourcePatchArgsDict']]
    """
    Source for the environment variable's value. Cannot be used if value is not empty.
    """

class EnvVarSourcePatchArgsDict(TypedDict):
    """
    EnvVarSource represents a source for the value of an EnvVar.
    """
    config_map_key_ref: NotRequired[Input['ConfigMapKeySelectorPatchArgsDict']]
    """
    Selects a key of a ConfigMap.
    """
    field_ref: NotRequired[Input['ObjectFieldSelectorPatchArgsDict']]
    """
    Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.
    """
    resource_field_ref: NotRequired[Input['ResourceFieldSelectorPatchArgsDict']]
    """
    Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
    """
    secret_key_ref: NotRequired[Input['SecretKeySelectorPatchArgsDict']]
    """
    Selects a key of a secret in the pod's namespace
    """

class EnvVarSourceArgsDict(TypedDict):
    """
    EnvVarSource represents a source for the value of an EnvVar.
    """
    config_map_key_ref: NotRequired[Input['ConfigMapKeySelectorArgsDict']]
    """
    Selects a key of a ConfigMap.
    """
    field_ref: NotRequired[Input['ObjectFieldSelectorArgsDict']]
    """
    Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.
    """
    resource_field_ref: NotRequired[Input['ResourceFieldSelectorArgsDict']]
    """
    Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.
    """
    secret_key_ref: NotRequired[Input['SecretKeySelectorArgsDict']]
    """
    Selects a key of a secret in the pod's namespace
    """

class EnvVarArgsDict(TypedDict):
    """
    EnvVar represents an environment variable present in a Container.
    """
    name: Input[str]
    """
    Name of the environment variable. Must be a C_IDENTIFIER.
    """
    value: NotRequired[Input[str]]
    """
    Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".
    """
    value_from: NotRequired[Input['EnvVarSourceArgsDict']]
    """
    Source for the environment variable's value. Cannot be used if value is not empty.
    """

class EphemeralContainerPatchArgsDict(TypedDict):
    """
    An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.

    To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.
    """
    args: NotRequired[Input[Sequence[Input[str]]]]
    """
    Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    """
    command: NotRequired[Input[Sequence[Input[str]]]]
    """
    Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    """
    env: NotRequired[Input[Sequence[Input['EnvVarPatchArgsDict']]]]
    """
    List of environment variables to set in the container. Cannot be updated.
    """
    env_from: NotRequired[Input[Sequence[Input['EnvFromSourcePatchArgsDict']]]]
    """
    List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.
    """
    image: NotRequired[Input[str]]
    """
    Container image name. More info: https://kubernetes.io/docs/concepts/containers/images
    """
    image_pull_policy: NotRequired[Input[str]]
    """
    Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images
    """
    lifecycle: NotRequired[Input['LifecyclePatchArgsDict']]
    """
    Lifecycle is not allowed for ephemeral containers.
    """
    liveness_probe: NotRequired[Input['ProbePatchArgsDict']]
    """
    Probes are not allowed for ephemeral containers.
    """
    name: NotRequired[Input[str]]
    """
    Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.
    """
    ports: NotRequired[Input[Sequence[Input['ContainerPortPatchArgsDict']]]]
    """
    Ports are not allowed for ephemeral containers.
    """
    readiness_probe: NotRequired[Input['ProbePatchArgsDict']]
    """
    Probes are not allowed for ephemeral containers.
    """
    resize_policy: NotRequired[Input[Sequence[Input['ContainerResizePolicyPatchArgsDict']]]]
    """
    Resources resize policy for the container.
    """
    resources: NotRequired[Input['ResourceRequirementsPatchArgsDict']]
    """
    Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.
    """
    restart_policy: NotRequired[Input[str]]
    """
    Restart policy for the container to manage the restart behavior of each container within a pod. This may only be set for init containers. You cannot set this field on ephemeral containers.
    """
    security_context: NotRequired[Input['SecurityContextPatchArgsDict']]
    """
    Optional: SecurityContext defines the security options the ephemeral container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext.
    """
    startup_probe: NotRequired[Input['ProbePatchArgsDict']]
    """
    Probes are not allowed for ephemeral containers.
    """
    stdin: NotRequired[Input[bool]]
    """
    Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.
    """
    stdin_once: NotRequired[Input[bool]]
    """
    Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false
    """
    target_container_name: NotRequired[Input[str]]
    """
    If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.

    The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined.
    """
    termination_message_path: NotRequired[Input[str]]
    """
    Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.
    """
    termination_message_policy: NotRequired[Input[str]]
    """
    Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.
    """
    tty: NotRequired[Input[bool]]
    """
    Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.
    """
    volume_devices: NotRequired[Input[Sequence[Input['VolumeDevicePatchArgsDict']]]]
    """
    volumeDevices is the list of block devices to be used by the container.
    """
    volume_mounts: NotRequired[Input[Sequence[Input['VolumeMountPatchArgsDict']]]]
    """
    Pod volumes to mount into the container's filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated.
    """
    working_dir: NotRequired[Input[str]]
    """
    Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.
    """

class EphemeralContainerArgsDict(TypedDict):
    """
    An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.

    To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.
    """
    name: Input[str]
    """
    Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.
    """
    args: NotRequired[Input[Sequence[Input[str]]]]
    """
    Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    """
    command: NotRequired[Input[Sequence[Input[str]]]]
    """
    Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
    """
    env: NotRequired[Input[Sequence[Input['EnvVarArgsDict']]]]
    """
    List of environment variables to set in the container. Cannot be updated.
    """
    env_from: NotRequired[Input[Sequence[Input['EnvFromSourceArgsDict']]]]
    """
    List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.
    """
    image: NotRequired[Input[str]]
    """
    Container image name. More info: https://kubernetes.io/docs/concepts/containers/images
    """
    image_pull_policy: NotRequired[Input[str]]
    """
    Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images
    """
    lifecycle: NotRequired[Input['LifecycleArgsDict']]
    """
    Lifecycle is not allowed for ephemeral containers.
    """
    liveness_probe: NotRequired[Input['ProbeArgsDict']]
    """
    Probes are not allowed for ephemeral containers.
    """
    ports: NotRequired[Input[Sequence[Input['ContainerPortArgsDict']]]]
    """
    Ports are not allowed for ephemeral containers.
    """
    readiness_probe: NotRequired[Input['ProbeArgsDict']]
    """
    Probes are not allowed for ephemeral containers.
    """
    resize_policy: NotRequired[Input[Sequence[Input['ContainerResizePolicyArgsDict']]]]
    """
    Resources resize policy for the container.
    """
    resources: NotRequired[Input['ResourceRequirementsArgsDict']]
    """
    Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.
    """
    restart_policy: NotRequired[Input[str]]
    """
    Restart policy for the container to manage the restart behavior of each container within a pod. This may only be set for init containers. You cannot set this field on ephemeral containers.
    """
    security_context: NotRequired[Input['SecurityContextArgsDict']]
    """
    Optional: SecurityContext defines the security options the ephemeral container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext.
    """
    startup_probe: NotRequired[Input['ProbeArgsDict']]
    """
    Probes are not allowed for ephemeral containers.
    """
    stdin: NotRequired[Input[bool]]
    """
    Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.
    """
    stdin_once: NotRequired[Input[bool]]
    """
    Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false
    """
    target_container_name: NotRequired[Input[str]]
    """
    If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.

    The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined.
    """
    termination_message_path: NotRequired[Input[str]]
    """
    Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.
    """
    termination_message_policy: NotRequired[Input[str]]
    """
    Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.
    """
    tty: NotRequired[Input[bool]]
    """
    Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.
    """
    volume_devices: NotRequired[Input[Sequence[Input['VolumeDeviceArgsDict']]]]
    """
    volumeDevices is the list of block devices to be used by the container.
    """
    volume_mounts: NotRequired[Input[Sequence[Input['VolumeMountArgsDict']]]]
    """
    Pod volumes to mount into the container's filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated.
    """
    working_dir: NotRequired[Input[str]]
    """
    Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.
    """

class EphemeralVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents an ephemeral volume that is handled by a normal storage driver.
    """
    read_only: NotRequired[Input[bool]]
    """
    Specifies a read-only configuration for the volume. Defaults to false (read/write).
    """
    volume_claim_template: NotRequired[Input['PersistentVolumeClaimTemplatePatchArgsDict']]
    """
    Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod.  The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).

    An existing PVC with that name that is not owned by the pod will *not* be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.

    This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.

    Required, must not be nil.
    """

class EphemeralVolumeSourceArgsDict(TypedDict):
    """
    Represents an ephemeral volume that is handled by a normal storage driver.
    """
    read_only: NotRequired[Input[bool]]
    """
    Specifies a read-only configuration for the volume. Defaults to false (read/write).
    """
    volume_claim_template: NotRequired[Input['PersistentVolumeClaimTemplateArgsDict']]
    """
    Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod.  The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).

    An existing PVC with that name that is not owned by the pod will *not* be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.

    This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.

    Required, must not be nil.
    """

class EventSeriesPatchArgsDict(TypedDict):
    """
    EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time.
    """
    count: NotRequired[Input[int]]
    """
    Number of occurrences in this series up to the last heartbeat time
    """
    last_observed_time: NotRequired[Input[str]]
    """
    Time of the last occurrence observed
    """
    state: NotRequired[Input[str]]
    """
    State of this Series: Ongoing or Finished Deprecated. Planned removal for 1.18
    """

class EventSeriesArgsDict(TypedDict):
    """
    EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time.
    """
    count: NotRequired[Input[int]]
    """
    Number of occurrences in this series up to the last heartbeat time
    """
    last_observed_time: NotRequired[Input[str]]
    """
    Time of the last occurrence observed
    """
    state: NotRequired[Input[str]]
    """
    State of this Series: Ongoing or Finished Deprecated. Planned removal for 1.18
    """

class EventSourcePatchArgsDict(TypedDict):
    """
    EventSource contains information for an event.
    """
    component: NotRequired[Input[str]]
    """
    Component from which the event is generated.
    """
    host: NotRequired[Input[str]]
    """
    Node name on which the event is generated.
    """

class EventSourceArgsDict(TypedDict):
    """
    EventSource contains information for an event.
    """
    component: NotRequired[Input[str]]
    """
    Component from which the event is generated.
    """
    host: NotRequired[Input[str]]
    """
    Node name on which the event is generated.
    """

class EventArgsDict(TypedDict):
    """
    Event is a report of an event somewhere in the cluster.  Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data.
    """
    involved_object: Input['ObjectReferenceArgsDict']
    """
    The object that this event is about.
    """
    metadata: Input['ObjectMetaArgsDict']
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    action: NotRequired[Input[str]]
    """
    What action was taken/failed regarding to the Regarding object.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    count: NotRequired[Input[int]]
    """
    The number of times this event has occurred.
    """
    event_time: NotRequired[Input[str]]
    """
    Time when this Event was first observed.
    """
    first_timestamp: NotRequired[Input[str]]
    """
    The time at which the event was first recorded. (Time of server receipt is in Type)
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    last_timestamp: NotRequired[Input[str]]
    """
    The time at which the most recent occurrence of this event was recorded.
    """
    message: NotRequired[Input[str]]
    """
    A human-readable description of the status of this operation.
    """
    reason: NotRequired[Input[str]]
    """
    This should be a short, machine understandable string that gives the reason for the transition into the object's current status.
    """
    related: NotRequired[Input['ObjectReferenceArgsDict']]
    """
    Optional secondary object for more complex actions.
    """
    reporting_component: NotRequired[Input[str]]
    """
    Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.
    """
    reporting_instance: NotRequired[Input[str]]
    """
    ID of the controller instance, e.g. `kubelet-xyzf`.
    """
    series: NotRequired[Input['EventSeriesArgsDict']]
    """
    Data about the Event series this event represents or nil if it's a singleton Event.
    """
    source: NotRequired[Input['EventSourceArgsDict']]
    """
    The component reporting this event. Should be a short machine understandable string.
    """
    type: NotRequired[Input[str]]
    """
    Type of this event (Normal, Warning), new types could be added in the future
    """

class ExecActionPatchArgsDict(TypedDict):
    """
    ExecAction describes a "run in container" action.
    """
    command: NotRequired[Input[Sequence[Input[str]]]]
    """
    Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """

class ExecActionArgsDict(TypedDict):
    """
    ExecAction describes a "run in container" action.
    """
    command: NotRequired[Input[Sequence[Input[str]]]]
    """
    Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.
    """

class FCVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    lun: NotRequired[Input[int]]
    """
    lun is Optional: FC target lun number
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    target_wwns: NotRequired[Input[Sequence[Input[str]]]]
    """
    targetWWNs is Optional: FC target worldwide names (WWNs)
    """
    wwids: NotRequired[Input[Sequence[Input[str]]]]
    """
    wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.
    """

class FCVolumeSourceArgsDict(TypedDict):
    """
    Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    lun: NotRequired[Input[int]]
    """
    lun is Optional: FC target lun number
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    target_wwns: NotRequired[Input[Sequence[Input[str]]]]
    """
    targetWWNs is Optional: FC target worldwide names (WWNs)
    """
    wwids: NotRequired[Input[Sequence[Input[str]]]]
    """
    wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.
    """

class FlexPersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin.
    """
    driver: NotRequired[Input[str]]
    """
    driver is the name of the driver to use for this volume.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.
    """
    options: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    options is Optional: this field holds extra command options if any.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    secretRef is Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    """

class FlexPersistentVolumeSourceArgsDict(TypedDict):
    """
    FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin.
    """
    driver: Input[str]
    """
    driver is the name of the driver to use for this volume.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.
    """
    options: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    options is Optional: this field holds extra command options if any.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    secretRef is Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    """

class FlexVolumeSourcePatchArgsDict(TypedDict):
    """
    FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    """
    driver: NotRequired[Input[str]]
    """
    driver is the name of the driver to use for this volume.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.
    """
    options: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    options is Optional: this field holds extra command options if any.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['LocalObjectReferencePatchArgsDict']]
    """
    secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    """

class FlexVolumeSourceArgsDict(TypedDict):
    """
    FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    """
    driver: Input[str]
    """
    driver is the name of the driver to use for this volume.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.
    """
    options: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    options is Optional: this field holds extra command options if any.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['LocalObjectReferenceArgsDict']]
    """
    secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.
    """

class FlockerVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.
    """
    dataset_name: NotRequired[Input[str]]
    """
    datasetName is Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated
    """
    dataset_uuid: NotRequired[Input[str]]
    """
    datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset
    """

class FlockerVolumeSourceArgsDict(TypedDict):
    """
    Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.
    """
    dataset_name: NotRequired[Input[str]]
    """
    datasetName is Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated
    """
    dataset_uuid: NotRequired[Input[str]]
    """
    datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset
    """

class GCEPersistentDiskVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Persistent Disk resource in Google Compute Engine.

    A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    partition: NotRequired[Input[int]]
    """
    partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    pd_name: NotRequired[Input[str]]
    """
    pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """

class GCEPersistentDiskVolumeSourceArgsDict(TypedDict):
    """
    Represents a Persistent Disk resource in Google Compute Engine.

    A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.
    """
    pd_name: Input[str]
    """
    pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    partition: NotRequired[Input[int]]
    """
    partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """

class GRPCActionPatchArgsDict(TypedDict):
    port: NotRequired[Input[int]]
    """
    Port number of the gRPC service. Number must be in the range 1 to 65535.
    """
    service: NotRequired[Input[str]]
    """
    Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).

    If this is not specified, the default behavior is defined by gRPC.
    """

class GRPCActionArgsDict(TypedDict):
    port: Input[int]
    """
    Port number of the gRPC service. Number must be in the range 1 to 65535.
    """
    service: NotRequired[Input[str]]
    """
    Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).

    If this is not specified, the default behavior is defined by gRPC.
    """

class GitRepoVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.

    DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    """
    directory: NotRequired[Input[str]]
    """
    directory is the target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.
    """
    repository: NotRequired[Input[str]]
    """
    repository is the URL
    """
    revision: NotRequired[Input[str]]
    """
    revision is the commit hash for the specified revision.
    """

class GitRepoVolumeSourceArgsDict(TypedDict):
    """
    Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.

    DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    """
    repository: Input[str]
    """
    repository is the URL
    """
    directory: NotRequired[Input[str]]
    """
    directory is the target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.
    """
    revision: NotRequired[Input[str]]
    """
    revision is the commit hash for the specified revision.
    """

class GlusterfsPersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.
    """
    endpoints: NotRequired[Input[str]]
    """
    endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    endpoints_namespace: NotRequired[Input[str]]
    """
    endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    path: NotRequired[Input[str]]
    """
    path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """

class GlusterfsPersistentVolumeSourceArgsDict(TypedDict):
    """
    Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.
    """
    endpoints: Input[str]
    """
    endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    path: Input[str]
    """
    path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    endpoints_namespace: NotRequired[Input[str]]
    """
    endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """

class GlusterfsVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.
    """
    endpoints: NotRequired[Input[str]]
    """
    endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    path: NotRequired[Input[str]]
    """
    path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """

class GlusterfsVolumeSourceArgsDict(TypedDict):
    """
    Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.
    """
    endpoints: Input[str]
    """
    endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    path: Input[str]
    """
    path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
    """

class HTTPGetActionPatchArgsDict(TypedDict):
    """
    HTTPGetAction describes an action based on HTTP Get requests.
    """
    host: NotRequired[Input[str]]
    """
    Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    """
    http_headers: NotRequired[Input[Sequence[Input['HTTPHeaderPatchArgsDict']]]]
    """
    Custom headers to set in the request. HTTP allows repeated headers.
    """
    path: NotRequired[Input[str]]
    """
    Path to access on the HTTP server.
    """
    port: NotRequired[Input[Union[int, str]]]
    """
    Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    """
    scheme: NotRequired[Input[str]]
    """
    Scheme to use for connecting to the host. Defaults to HTTP.
    """

class HTTPGetActionArgsDict(TypedDict):
    """
    HTTPGetAction describes an action based on HTTP Get requests.
    """
    port: Input[Union[int, str]]
    """
    Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    """
    host: NotRequired[Input[str]]
    """
    Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.
    """
    http_headers: NotRequired[Input[Sequence[Input['HTTPHeaderArgsDict']]]]
    """
    Custom headers to set in the request. HTTP allows repeated headers.
    """
    path: NotRequired[Input[str]]
    """
    Path to access on the HTTP server.
    """
    scheme: NotRequired[Input[str]]
    """
    Scheme to use for connecting to the host. Defaults to HTTP.
    """

class HTTPHeaderPatchArgsDict(TypedDict):
    """
    HTTPHeader describes a custom header to be used in HTTP probes
    """
    name: NotRequired[Input[str]]
    """
    The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.
    """
    value: NotRequired[Input[str]]
    """
    The header field value
    """

class HTTPHeaderArgsDict(TypedDict):
    """
    HTTPHeader describes a custom header to be used in HTTP probes
    """
    name: Input[str]
    """
    The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.
    """
    value: Input[str]
    """
    The header field value
    """

class HostAliasPatchArgsDict(TypedDict):
    """
    HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
    """
    hostnames: NotRequired[Input[Sequence[Input[str]]]]
    """
    Hostnames for the above IP address.
    """
    ip: NotRequired[Input[str]]
    """
    IP address of the host file entry.
    """

class HostAliasArgsDict(TypedDict):
    """
    HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.
    """
    hostnames: NotRequired[Input[Sequence[Input[str]]]]
    """
    Hostnames for the above IP address.
    """
    ip: NotRequired[Input[str]]
    """
    IP address of the host file entry.
    """

class HostIPArgsDict(TypedDict):
    """
    HostIP represents a single IP address allocated to the host.
    """
    ip: NotRequired[Input[str]]
    """
    IP is the IP address assigned to the host
    """

class HostPathVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.
    """
    path: NotRequired[Input[str]]
    """
    path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    type: NotRequired[Input[str]]
    """
    type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """

class HostPathVolumeSourceArgsDict(TypedDict):
    """
    Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.
    """
    path: Input[str]
    """
    path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    type: NotRequired[Input[str]]
    """
    type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """

class ISCSIPersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.
    """
    chap_auth_discovery: NotRequired[Input[bool]]
    """
    chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication
    """
    chap_auth_session: NotRequired[Input[bool]]
    """
    chapAuthSession defines whether support iSCSI Session CHAP authentication
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi
    """
    initiator_name: NotRequired[Input[str]]
    """
    initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.
    """
    iqn: NotRequired[Input[str]]
    """
    iqn is Target iSCSI Qualified Name.
    """
    iscsi_interface: NotRequired[Input[str]]
    """
    iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).
    """
    lun: NotRequired[Input[int]]
    """
    lun is iSCSI Target Lun number.
    """
    portals: NotRequired[Input[Sequence[Input[str]]]]
    """
    portals is the iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
    """
    secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    secretRef is the CHAP Secret for iSCSI target and initiator authentication
    """
    target_portal: NotRequired[Input[str]]
    """
    targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    """

class ISCSIPersistentVolumeSourceArgsDict(TypedDict):
    """
    ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.
    """
    iqn: Input[str]
    """
    iqn is Target iSCSI Qualified Name.
    """
    lun: Input[int]
    """
    lun is iSCSI Target Lun number.
    """
    target_portal: Input[str]
    """
    targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    """
    chap_auth_discovery: NotRequired[Input[bool]]
    """
    chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication
    """
    chap_auth_session: NotRequired[Input[bool]]
    """
    chapAuthSession defines whether support iSCSI Session CHAP authentication
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi
    """
    initiator_name: NotRequired[Input[str]]
    """
    initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.
    """
    iscsi_interface: NotRequired[Input[str]]
    """
    iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).
    """
    portals: NotRequired[Input[Sequence[Input[str]]]]
    """
    portals is the iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
    """
    secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    secretRef is the CHAP Secret for iSCSI target and initiator authentication
    """

class ISCSIVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.
    """
    chap_auth_discovery: NotRequired[Input[bool]]
    """
    chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication
    """
    chap_auth_session: NotRequired[Input[bool]]
    """
    chapAuthSession defines whether support iSCSI Session CHAP authentication
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi
    """
    initiator_name: NotRequired[Input[str]]
    """
    initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.
    """
    iqn: NotRequired[Input[str]]
    """
    iqn is the target iSCSI Qualified Name.
    """
    iscsi_interface: NotRequired[Input[str]]
    """
    iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).
    """
    lun: NotRequired[Input[int]]
    """
    lun represents iSCSI Target Lun number.
    """
    portals: NotRequired[Input[Sequence[Input[str]]]]
    """
    portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
    """
    secret_ref: NotRequired[Input['LocalObjectReferencePatchArgsDict']]
    """
    secretRef is the CHAP Secret for iSCSI target and initiator authentication
    """
    target_portal: NotRequired[Input[str]]
    """
    targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    """

class ISCSIVolumeSourceArgsDict(TypedDict):
    """
    Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.
    """
    iqn: Input[str]
    """
    iqn is the target iSCSI Qualified Name.
    """
    lun: Input[int]
    """
    lun represents iSCSI Target Lun number.
    """
    target_portal: Input[str]
    """
    targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    """
    chap_auth_discovery: NotRequired[Input[bool]]
    """
    chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication
    """
    chap_auth_session: NotRequired[Input[bool]]
    """
    chapAuthSession defines whether support iSCSI Session CHAP authentication
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi
    """
    initiator_name: NotRequired[Input[str]]
    """
    initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.
    """
    iscsi_interface: NotRequired[Input[str]]
    """
    iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).
    """
    portals: NotRequired[Input[Sequence[Input[str]]]]
    """
    portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
    """
    secret_ref: NotRequired[Input['LocalObjectReferenceArgsDict']]
    """
    secretRef is the CHAP Secret for iSCSI target and initiator authentication
    """

class KeyToPathPatchArgsDict(TypedDict):
    """
    Maps a string key to a path within a volume.
    """
    key: NotRequired[Input[str]]
    """
    key is the key to project.
    """
    mode: NotRequired[Input[int]]
    """
    mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    path: NotRequired[Input[str]]
    """
    path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    """

class KeyToPathArgsDict(TypedDict):
    """
    Maps a string key to a path within a volume.
    """
    key: Input[str]
    """
    key is the key to project.
    """
    path: Input[str]
    """
    path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.
    """
    mode: NotRequired[Input[int]]
    """
    mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """

class LifecycleHandlerPatchArgsDict(TypedDict):
    """
    LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.
    """
    exec_: NotRequired[Input['ExecActionPatchArgsDict']]
    """
    Exec specifies the action to take.
    """
    http_get: NotRequired[Input['HTTPGetActionPatchArgsDict']]
    """
    HTTPGet specifies the http request to perform.
    """
    sleep: NotRequired[Input['SleepActionPatchArgsDict']]
    """
    Sleep represents the duration that the container should sleep before being terminated.
    """
    tcp_socket: NotRequired[Input['TCPSocketActionPatchArgsDict']]
    """
    Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified.
    """

class LifecycleHandlerArgsDict(TypedDict):
    """
    LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.
    """
    exec_: NotRequired[Input['ExecActionArgsDict']]
    """
    Exec specifies the action to take.
    """
    http_get: NotRequired[Input['HTTPGetActionArgsDict']]
    """
    HTTPGet specifies the http request to perform.
    """
    sleep: NotRequired[Input['SleepActionArgsDict']]
    """
    Sleep represents the duration that the container should sleep before being terminated.
    """
    tcp_socket: NotRequired[Input['TCPSocketActionArgsDict']]
    """
    Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified.
    """

class LifecyclePatchArgsDict(TypedDict):
    """
    Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.
    """
    post_start: NotRequired[Input['LifecycleHandlerPatchArgsDict']]
    """
    PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    """
    pre_stop: NotRequired[Input['LifecycleHandlerPatchArgsDict']]
    """
    PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod's termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    """

class LifecycleArgsDict(TypedDict):
    """
    Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.
    """
    post_start: NotRequired[Input['LifecycleHandlerArgsDict']]
    """
    PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    """
    pre_stop: NotRequired[Input['LifecycleHandlerArgsDict']]
    """
    PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod's termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
    """

class LimitRangeItemPatchArgsDict(TypedDict):
    """
    LimitRangeItem defines a min/max usage limit for any resource that matches on kind.
    """
    default: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Default resource requirement limit value by resource name if resource limit is omitted.
    """
    default_request: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.
    """
    max: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Max usage constraints on this kind by resource name.
    """
    max_limit_request_ratio: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.
    """
    min: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Min usage constraints on this kind by resource name.
    """
    type: NotRequired[Input[str]]
    """
    Type of resource that this limit applies to.
    """

class LimitRangeItemArgsDict(TypedDict):
    """
    LimitRangeItem defines a min/max usage limit for any resource that matches on kind.
    """
    type: Input[str]
    """
    Type of resource that this limit applies to.
    """
    default: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Default resource requirement limit value by resource name if resource limit is omitted.
    """
    default_request: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.
    """
    max: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Max usage constraints on this kind by resource name.
    """
    max_limit_request_ratio: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.
    """
    min: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Min usage constraints on this kind by resource name.
    """

class LimitRangeSpecPatchArgsDict(TypedDict):
    """
    LimitRangeSpec defines a min/max usage limit for resources that match on kind.
    """
    limits: NotRequired[Input[Sequence[Input['LimitRangeItemPatchArgsDict']]]]
    """
    Limits is the list of LimitRangeItem objects that are enforced.
    """

class LimitRangeSpecArgsDict(TypedDict):
    """
    LimitRangeSpec defines a min/max usage limit for resources that match on kind.
    """
    limits: Input[Sequence[Input['LimitRangeItemArgsDict']]]
    """
    Limits is the list of LimitRangeItem objects that are enforced.
    """

class LimitRangeArgsDict(TypedDict):
    """
    LimitRange sets resource usage limits for each kind of resource in a Namespace.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['LimitRangeSpecArgsDict']]
    """
    Spec defines the limits enforced. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class LoadBalancerIngressArgsDict(TypedDict):
    """
    LoadBalancerIngress represents the status of a load-balancer ingress point: traffic intended for the service should be sent to an ingress point.
    """
    hostname: NotRequired[Input[str]]
    """
    Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers)
    """
    ip: NotRequired[Input[str]]
    """
    IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers)
    """
    ip_mode: NotRequired[Input[str]]
    """
    IPMode specifies how the load-balancer IP behaves, and may only be specified when the ip field is specified. Setting this to "VIP" indicates that traffic is delivered to the node with the destination set to the load-balancer's IP and port. Setting this to "Proxy" indicates that traffic is delivered to the node or pod with the destination set to the node's IP and node port or the pod's IP and port. Service implementations may use this information to adjust traffic routing.
    """
    ports: NotRequired[Input[Sequence[Input['PortStatusArgsDict']]]]
    """
    Ports is a list of records of service ports If used, every port defined in the service should have an entry in it
    """

class LoadBalancerStatusArgsDict(TypedDict):
    """
    LoadBalancerStatus represents the status of a load-balancer.
    """
    ingress: NotRequired[Input[Sequence[Input['LoadBalancerIngressArgsDict']]]]
    """
    Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.
    """

class LocalObjectReferencePatchArgsDict(TypedDict):
    """
    LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """

class LocalObjectReferenceArgsDict(TypedDict):
    """
    LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """

class LocalVolumeSourcePatchArgsDict(TypedDict):
    """
    Local represents directly-attached storage with node affinity (Beta feature)
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified.
    """
    path: NotRequired[Input[str]]
    """
    path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, ...).
    """

class LocalVolumeSourceArgsDict(TypedDict):
    """
    Local represents directly-attached storage with node affinity (Beta feature)
    """
    path: Input[str]
    """
    path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, ...).
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified.
    """

class ModifyVolumeStatusPatchArgsDict(TypedDict):
    """
    ModifyVolumeStatus represents the status object of ControllerModifyVolume operation
    """
    status: NotRequired[Input[str]]
    """
    status is the status of the ControllerModifyVolume operation. It can be in any of following states:
     - Pending
       Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as
       the specified VolumeAttributesClass not existing.
     - InProgress
       InProgress indicates that the volume is being modified.
     - Infeasible
      Infeasible indicates that the request has been rejected as invalid by the CSI driver. To
    	  resolve the error, a valid VolumeAttributesClass needs to be specified.
    Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.
    """
    target_volume_attributes_class_name: NotRequired[Input[str]]
    """
    targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled
    """

class ModifyVolumeStatusArgsDict(TypedDict):
    """
    ModifyVolumeStatus represents the status object of ControllerModifyVolume operation
    """
    status: Input[str]
    """
    status is the status of the ControllerModifyVolume operation. It can be in any of following states:
     - Pending
       Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as
       the specified VolumeAttributesClass not existing.
     - InProgress
       InProgress indicates that the volume is being modified.
     - Infeasible
      Infeasible indicates that the request has been rejected as invalid by the CSI driver. To
    	  resolve the error, a valid VolumeAttributesClass needs to be specified.
    Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.
    """
    target_volume_attributes_class_name: NotRequired[Input[str]]
    """
    targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled
    """

class NFSVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.
    """
    path: NotRequired[Input[str]]
    """
    path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    server: NotRequired[Input[str]]
    """
    server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """

class NFSVolumeSourceArgsDict(TypedDict):
    """
    Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.
    """
    path: Input[str]
    """
    path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    server: Input[str]
    """
    server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """

class NamespaceConditionArgsDict(TypedDict):
    """
    NamespaceCondition contains details about state of namespace.
    """
    status: Input[str]
    """
    Status of the condition, one of True, False, Unknown.
    """
    type: Input[str]
    """
    Type of namespace controller condition.
    """
    last_transition_time: NotRequired[Input[str]]
    message: NotRequired[Input[str]]
    reason: NotRequired[Input[str]]

class NamespaceSpecPatchArgsDict(TypedDict):
    """
    NamespaceSpec describes the attributes on a Namespace.
    """
    finalizers: NotRequired[Input[Sequence[Input[str]]]]
    """
    Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
    """

class NamespaceSpecArgsDict(TypedDict):
    """
    NamespaceSpec describes the attributes on a Namespace.
    """
    finalizers: NotRequired[Input[Sequence[Input[str]]]]
    """
    Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
    """

class NamespaceStatusArgsDict(TypedDict):
    """
    NamespaceStatus is information about the current status of a Namespace.
    """
    conditions: NotRequired[Input[Sequence[Input['NamespaceConditionArgsDict']]]]
    """
    Represents the latest available observations of a namespace's current state.
    """
    phase: NotRequired[Input[str]]
    """
    Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
    """

class NamespaceArgsDict(TypedDict):
    """
    Namespace provides a scope for Names. Use of multiple namespaces is optional.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['NamespaceSpecArgsDict']]
    """
    Spec defines the behavior of the Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    status: NotRequired[Input['NamespaceStatusArgsDict']]
    """
    Status describes the current status of a Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class NodeAddressArgsDict(TypedDict):
    """
    NodeAddress contains information for the node's address.
    """
    address: Input[str]
    """
    The node address.
    """
    type: Input[str]
    """
    Node address type, one of Hostname, ExternalIP or InternalIP.
    """

class NodeAffinityPatchArgsDict(TypedDict):
    """
    Node affinity is a group of node affinity scheduling rules.
    """
    preferred_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['PreferredSchedulingTermPatchArgsDict']]]]
    """
    The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
    """
    required_during_scheduling_ignored_during_execution: NotRequired[Input['NodeSelectorPatchArgsDict']]
    """
    If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    """

class NodeAffinityArgsDict(TypedDict):
    """
    Node affinity is a group of node affinity scheduling rules.
    """
    preferred_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['PreferredSchedulingTermArgsDict']]]]
    """
    The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
    """
    required_during_scheduling_ignored_during_execution: NotRequired[Input['NodeSelectorArgsDict']]
    """
    If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
    """

class NodeConditionArgsDict(TypedDict):
    """
    NodeCondition contains condition information for a node.
    """
    status: Input[str]
    """
    Status of the condition, one of True, False, Unknown.
    """
    type: Input[str]
    """
    Type of node condition.
    """
    last_heartbeat_time: NotRequired[Input[str]]
    """
    Last time we got an update on a given condition.
    """
    last_transition_time: NotRequired[Input[str]]
    """
    Last time the condition transit from one status to another.
    """
    message: NotRequired[Input[str]]
    """
    Human readable message indicating details about last transition.
    """
    reason: NotRequired[Input[str]]
    """
    (brief) reason for the condition's last transition.
    """

class NodeConfigSourcePatchArgsDict(TypedDict):
    """
    NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22
    """
    config_map: NotRequired[Input['ConfigMapNodeConfigSourcePatchArgsDict']]
    """
    ConfigMap is a reference to a Node's ConfigMap
    """

class NodeConfigSourceArgsDict(TypedDict):
    """
    NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22
    """
    config_map: NotRequired[Input['ConfigMapNodeConfigSourceArgsDict']]
    """
    ConfigMap is a reference to a Node's ConfigMap
    """

class NodeConfigStatusArgsDict(TypedDict):
    """
    NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource.
    """
    active: NotRequired[Input['NodeConfigSourceArgsDict']]
    """
    Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error.
    """
    assigned: NotRequired[Input['NodeConfigSourceArgsDict']]
    """
    Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned.
    """
    error: NotRequired[Input[str]]
    """
    Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.
    """
    last_known_good: NotRequired[Input['NodeConfigSourceArgsDict']]
    """
    LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future.
    """

class NodeDaemonEndpointsArgsDict(TypedDict):
    """
    NodeDaemonEndpoints lists ports opened by daemons running on the Node.
    """
    kubelet_endpoint: NotRequired[Input['DaemonEndpointArgsDict']]
    """
    Endpoint on which Kubelet is listening.
    """

class NodeRuntimeHandlerFeaturesArgsDict(TypedDict):
    """
    NodeRuntimeHandlerFeatures is a set of runtime features.
    """
    recursive_read_only_mounts: NotRequired[Input[bool]]
    """
    RecursiveReadOnlyMounts is set to true if the runtime handler supports RecursiveReadOnlyMounts.
    """

class NodeRuntimeHandlerArgsDict(TypedDict):
    """
    NodeRuntimeHandler is a set of runtime handler information.
    """
    features: NotRequired[Input['NodeRuntimeHandlerFeaturesArgsDict']]
    """
    Supported features.
    """
    name: NotRequired[Input[str]]
    """
    Runtime handler name. Empty for the default runtime handler.
    """

class NodeSelectorPatchArgsDict(TypedDict):
    """
    A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.
    """
    node_selector_terms: NotRequired[Input[Sequence[Input['NodeSelectorTermPatchArgsDict']]]]
    """
    Required. A list of node selector terms. The terms are ORed.
    """

class NodeSelectorRequirementPatchArgsDict(TypedDict):
    """
    A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    """
    key: NotRequired[Input[str]]
    """
    The label key that the selector applies to.
    """
    operator: NotRequired[Input[str]]
    """
    Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    """
    values: NotRequired[Input[Sequence[Input[str]]]]
    """
    An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """

class NodeSelectorRequirementArgsDict(TypedDict):
    """
    A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.
    """
    key: Input[str]
    """
    The label key that the selector applies to.
    """
    operator: Input[str]
    """
    Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
    """
    values: NotRequired[Input[Sequence[Input[str]]]]
    """
    An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.
    """

class NodeSelectorTermPatchArgsDict(TypedDict):
    """
    A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
    """
    match_expressions: NotRequired[Input[Sequence[Input['NodeSelectorRequirementPatchArgsDict']]]]
    """
    A list of node selector requirements by node's labels.
    """
    match_fields: NotRequired[Input[Sequence[Input['NodeSelectorRequirementPatchArgsDict']]]]
    """
    A list of node selector requirements by node's fields.
    """

class NodeSelectorTermArgsDict(TypedDict):
    """
    A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.
    """
    match_expressions: NotRequired[Input[Sequence[Input['NodeSelectorRequirementArgsDict']]]]
    """
    A list of node selector requirements by node's labels.
    """
    match_fields: NotRequired[Input[Sequence[Input['NodeSelectorRequirementArgsDict']]]]
    """
    A list of node selector requirements by node's fields.
    """

class NodeSelectorArgsDict(TypedDict):
    """
    A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.
    """
    node_selector_terms: Input[Sequence[Input['NodeSelectorTermArgsDict']]]
    """
    Required. A list of node selector terms. The terms are ORed.
    """

class NodeSpecPatchArgsDict(TypedDict):
    """
    NodeSpec describes the attributes that a node is created with.
    """
    config_source: NotRequired[Input['NodeConfigSourcePatchArgsDict']]
    """
    Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed.
    """
    external_id: NotRequired[Input[str]]
    """
    Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966
    """
    pod_cidr: NotRequired[Input[str]]
    """
    PodCIDR represents the pod IP range assigned to the node.
    """
    pod_cidrs: NotRequired[Input[Sequence[Input[str]]]]
    """
    podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.
    """
    provider_id: NotRequired[Input[str]]
    """
    ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>
    """
    taints: NotRequired[Input[Sequence[Input['TaintPatchArgsDict']]]]
    """
    If specified, the node's taints.
    """
    unschedulable: NotRequired[Input[bool]]
    """
    Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration
    """

class NodeSpecArgsDict(TypedDict):
    """
    NodeSpec describes the attributes that a node is created with.
    """
    config_source: NotRequired[Input['NodeConfigSourceArgsDict']]
    """
    Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed.
    """
    external_id: NotRequired[Input[str]]
    """
    Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966
    """
    pod_cidr: NotRequired[Input[str]]
    """
    PodCIDR represents the pod IP range assigned to the node.
    """
    pod_cidrs: NotRequired[Input[Sequence[Input[str]]]]
    """
    podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.
    """
    provider_id: NotRequired[Input[str]]
    """
    ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>
    """
    taints: NotRequired[Input[Sequence[Input['TaintArgsDict']]]]
    """
    If specified, the node's taints.
    """
    unschedulable: NotRequired[Input[bool]]
    """
    Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration
    """

class NodeStatusArgsDict(TypedDict):
    """
    NodeStatus is information about the current status of a node.
    """
    addresses: NotRequired[Input[Sequence[Input['NodeAddressArgsDict']]]]
    """
    List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See https://pr.k8s.io/79391 for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node's address in its own status or consumers of the downward API (status.hostIP).
    """
    allocatable: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.
    """
    capacity: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity
    """
    conditions: NotRequired[Input[Sequence[Input['NodeConditionArgsDict']]]]
    """
    Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition
    """
    config: NotRequired[Input['NodeConfigStatusArgsDict']]
    """
    Status of the config assigned to the node via the dynamic Kubelet config feature.
    """
    daemon_endpoints: NotRequired[Input['NodeDaemonEndpointsArgsDict']]
    """
    Endpoints of daemons running on the Node.
    """
    images: NotRequired[Input[Sequence[Input['ContainerImageArgsDict']]]]
    """
    List of container images on this node
    """
    node_info: NotRequired[Input['NodeSystemInfoArgsDict']]
    """
    Set of ids/uuids to uniquely identify the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#info
    """
    phase: NotRequired[Input[str]]
    """
    NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated.
    """
    runtime_handlers: NotRequired[Input[Sequence[Input['NodeRuntimeHandlerArgsDict']]]]
    """
    The available runtime handlers.
    """
    volumes_attached: NotRequired[Input[Sequence[Input['AttachedVolumeArgsDict']]]]
    """
    List of volumes that are attached to the node.
    """
    volumes_in_use: NotRequired[Input[Sequence[Input[str]]]]
    """
    List of attachable volumes in use (mounted) by the node.
    """

class NodeSystemInfoArgsDict(TypedDict):
    """
    NodeSystemInfo is a set of ids/uuids to uniquely identify the node.
    """
    architecture: Input[str]
    """
    The Architecture reported by the node
    """
    boot_id: Input[str]
    """
    Boot ID reported by the node.
    """
    container_runtime_version: Input[str]
    """
    ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2).
    """
    kernel_version: Input[str]
    """
    Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).
    """
    kube_proxy_version: Input[str]
    """
    KubeProxy Version reported by the node.
    """
    kubelet_version: Input[str]
    """
    Kubelet Version reported by the node.
    """
    machine_id: Input[str]
    """
    MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html
    """
    operating_system: Input[str]
    """
    The Operating System reported by the node
    """
    os_image: Input[str]
    """
    OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).
    """
    system_uuid: Input[str]
    """
    SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid
    """

class NodeArgsDict(TypedDict):
    """
    Node is a worker node in Kubernetes. Each node will have a unique identifier in the cache (i.e. in etcd).
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['NodeSpecArgsDict']]
    """
    Spec defines the behavior of a node. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    status: NotRequired[Input['NodeStatusArgsDict']]
    """
    Most recently observed status of the node. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class ObjectFieldSelectorPatchArgsDict(TypedDict):
    """
    ObjectFieldSelector selects an APIVersioned field of an object.
    """
    api_version: NotRequired[Input[str]]
    """
    Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """
    field_path: NotRequired[Input[str]]
    """
    Path of the field to select in the specified API version.
    """

class ObjectFieldSelectorArgsDict(TypedDict):
    """
    ObjectFieldSelector selects an APIVersioned field of an object.
    """
    field_path: Input[str]
    """
    Path of the field to select in the specified API version.
    """
    api_version: NotRequired[Input[str]]
    """
    Version of the schema the FieldPath is written in terms of, defaults to "v1".
    """

class ObjectReferencePatchArgsDict(TypedDict):
    """
    ObjectReference contains enough information to let you inspect or modify the referred object.
    """
    api_version: NotRequired[Input[str]]
    """
    API version of the referent.
    """
    field_path: NotRequired[Input[str]]
    """
    If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.
    """
    kind: NotRequired[Input[str]]
    """
    Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    namespace: NotRequired[Input[str]]
    """
    Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
    """
    resource_version: NotRequired[Input[str]]
    """
    Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
    """
    uid: NotRequired[Input[str]]
    """
    UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids
    """

class ObjectReferenceArgsDict(TypedDict):
    """
    ObjectReference contains enough information to let you inspect or modify the referred object.
    """
    api_version: NotRequired[Input[str]]
    """
    API version of the referent.
    """
    field_path: NotRequired[Input[str]]
    """
    If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.
    """
    kind: NotRequired[Input[str]]
    """
    Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    namespace: NotRequired[Input[str]]
    """
    Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
    """
    resource_version: NotRequired[Input[str]]
    """
    Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency
    """
    uid: NotRequired[Input[str]]
    """
    UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids
    """

class PersistentVolumeClaimConditionPatchArgsDict(TypedDict):
    """
    PersistentVolumeClaimCondition contains details about state of pvc
    """
    last_probe_time: NotRequired[Input[str]]
    """
    lastProbeTime is the time we probed the condition.
    """
    last_transition_time: NotRequired[Input[str]]
    """
    lastTransitionTime is the time the condition transitioned from one status to another.
    """
    message: NotRequired[Input[str]]
    """
    message is the human-readable message indicating details about last transition.
    """
    reason: NotRequired[Input[str]]
    """
    reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "Resizing" that means the underlying persistent volume is being resized.
    """
    status: NotRequired[Input[str]]
    type: NotRequired[Input[str]]

class PersistentVolumeClaimConditionArgsDict(TypedDict):
    """
    PersistentVolumeClaimCondition contains details about state of pvc
    """
    status: Input[str]
    type: Input[str]
    last_probe_time: NotRequired[Input[str]]
    """
    lastProbeTime is the time we probed the condition.
    """
    last_transition_time: NotRequired[Input[str]]
    """
    lastTransitionTime is the time the condition transitioned from one status to another.
    """
    message: NotRequired[Input[str]]
    """
    message is the human-readable message indicating details about last transition.
    """
    reason: NotRequired[Input[str]]
    """
    reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "Resizing" that means the underlying persistent volume is being resized.
    """

class PersistentVolumeClaimPatchArgsDict(TypedDict):
    """
    PersistentVolumeClaim is a user's request for and claim to a persistent volume
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaPatchArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['PersistentVolumeClaimSpecPatchArgsDict']]
    """
    spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    status: NotRequired[Input['PersistentVolumeClaimStatusPatchArgsDict']]
    """
    status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """

class PersistentVolumeClaimSpecPatchArgsDict(TypedDict):
    """
    PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes
    """
    access_modes: NotRequired[Input[Sequence[Input[str]]]]
    """
    accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    """
    data_source: NotRequired[Input['TypedLocalObjectReferencePatchArgsDict']]
    """
    dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.
    """
    data_source_ref: NotRequired[Input['TypedObjectReferencePatchArgsDict']]
    """
    dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef
      allows any non-core object, as well as PersistentVolumeClaim objects.
    * While dataSource ignores disallowed values (dropping them), dataSourceRef
      preserves all values, and generates an error if a disallowed value is
      specified.
    * While dataSource only allows local objects, dataSourceRef allows objects
      in any namespaces.
    (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.
    """
    resources: NotRequired[Input['VolumeResourceRequirementsPatchArgsDict']]
    """
    resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
    """
    selector: NotRequired[Input['LabelSelectorPatchArgsDict']]
    """
    selector is a label query over volumes to consider for binding.
    """
    storage_class_name: NotRequired[Input[str]]
    """
    storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1
    """
    volume_attributes_class_name: NotRequired[Input[str]]
    """
    volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it's not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ (Alpha) Using this field requires the VolumeAttributesClass feature gate to be enabled.
    """
    volume_mode: NotRequired[Input[str]]
    """
    volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the binding reference to the PersistentVolume backing this claim.
    """

class PersistentVolumeClaimSpecArgsDict(TypedDict):
    """
    PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes
    """
    access_modes: NotRequired[Input[Sequence[Input[str]]]]
    """
    accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    """
    data_source: NotRequired[Input['TypedLocalObjectReferenceArgsDict']]
    """
    dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.
    """
    data_source_ref: NotRequired[Input['TypedObjectReferenceArgsDict']]
    """
    dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef
      allows any non-core object, as well as PersistentVolumeClaim objects.
    * While dataSource ignores disallowed values (dropping them), dataSourceRef
      preserves all values, and generates an error if a disallowed value is
      specified.
    * While dataSource only allows local objects, dataSourceRef allows objects
      in any namespaces.
    (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.
    """
    resources: NotRequired[Input['VolumeResourceRequirementsArgsDict']]
    """
    resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
    """
    selector: NotRequired[Input['LabelSelectorArgsDict']]
    """
    selector is a label query over volumes to consider for binding.
    """
    storage_class_name: NotRequired[Input[str]]
    """
    storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1
    """
    volume_attributes_class_name: NotRequired[Input[str]]
    """
    volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it's not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ (Alpha) Using this field requires the VolumeAttributesClass feature gate to be enabled.
    """
    volume_mode: NotRequired[Input[str]]
    """
    volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the binding reference to the PersistentVolume backing this claim.
    """

class PersistentVolumeClaimStatusPatchArgsDict(TypedDict):
    """
    PersistentVolumeClaimStatus is the current status of a persistent volume claim.
    """
    access_modes: NotRequired[Input[Sequence[Input[str]]]]
    """
    accessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    """
    allocated_resource_statuses: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:
    	* Un-prefixed keys:
    		- storage - the capacity of the volume.
    	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource"
    Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.

    ClaimResourceStatus can be in any of following states:
    	- ControllerResizeInProgress:
    		State set when resize controller starts resizing the volume in control-plane.
    	- ControllerResizeFailed:
    		State set when resize has failed in resize controller with a terminal error.
    	- NodeResizePending:
    		State set when resize controller has finished resizing the volume but further resizing of
    		volume is needed on the node.
    	- NodeResizeInProgress:
    		State set when kubelet starts resizing the volume.
    	- NodeResizeFailed:
    		State set when resizing has failed in kubelet with a terminal error. Transient errors don't set
    		NodeResizeFailed.
    For example: if expanding a PVC for more capacity - this field can be one of the following states:
    	- pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress"
         - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed"
         - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending"
         - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress"
         - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed"
    When this field is not set, it means that no resize operation is in progress for the given PVC.

    A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.

    This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.
    """
    allocated_resources: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either:
    	* Un-prefixed keys:
    		- storage - the capacity of the volume.
    	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource"
    Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.

    Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.

    A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.

    This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.
    """
    capacity: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    capacity represents the actual resources of the underlying volume.
    """
    conditions: NotRequired[Input[Sequence[Input['PersistentVolumeClaimConditionPatchArgsDict']]]]
    """
    conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.
    """
    current_volume_attributes_class_name: NotRequired[Input[str]]
    """
    currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim This is an alpha field and requires enabling VolumeAttributesClass feature.
    """
    modify_volume_status: NotRequired[Input['ModifyVolumeStatusPatchArgsDict']]
    """
    ModifyVolumeStatus represents the status object of ControllerModifyVolume operation. When this is unset, there is no ModifyVolume operation being attempted. This is an alpha field and requires enabling VolumeAttributesClass feature.
    """
    phase: NotRequired[Input[str]]
    """
    phase represents the current phase of PersistentVolumeClaim.
    """
    resize_status: NotRequired[Input[str]]
    """
    resizeStatus stores status of resize operation. ResizeStatus is not set by default but when expansion is complete resizeStatus is set to empty string by resize controller or kubelet. This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.
    """

class PersistentVolumeClaimStatusArgsDict(TypedDict):
    """
    PersistentVolumeClaimStatus is the current status of a persistent volume claim.
    """
    access_modes: NotRequired[Input[Sequence[Input[str]]]]
    """
    accessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1
    """
    allocated_resource_statuses: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:
    	* Un-prefixed keys:
    		- storage - the capacity of the volume.
    	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource"
    Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.

    ClaimResourceStatus can be in any of following states:
    	- ControllerResizeInProgress:
    		State set when resize controller starts resizing the volume in control-plane.
    	- ControllerResizeFailed:
    		State set when resize has failed in resize controller with a terminal error.
    	- NodeResizePending:
    		State set when resize controller has finished resizing the volume but further resizing of
    		volume is needed on the node.
    	- NodeResizeInProgress:
    		State set when kubelet starts resizing the volume.
    	- NodeResizeFailed:
    		State set when resizing has failed in kubelet with a terminal error. Transient errors don't set
    		NodeResizeFailed.
    For example: if expanding a PVC for more capacity - this field can be one of the following states:
    	- pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress"
         - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed"
         - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending"
         - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress"
         - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed"
    When this field is not set, it means that no resize operation is in progress for the given PVC.

    A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.

    This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.
    """
    allocated_resources: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either:
    	* Un-prefixed keys:
    		- storage - the capacity of the volume.
    	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource"
    Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.

    Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.

    A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.

    This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.
    """
    capacity: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    capacity represents the actual resources of the underlying volume.
    """
    conditions: NotRequired[Input[Sequence[Input['PersistentVolumeClaimConditionArgsDict']]]]
    """
    conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.
    """
    current_volume_attributes_class_name: NotRequired[Input[str]]
    """
    currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim This is an alpha field and requires enabling VolumeAttributesClass feature.
    """
    modify_volume_status: NotRequired[Input['ModifyVolumeStatusArgsDict']]
    """
    ModifyVolumeStatus represents the status object of ControllerModifyVolume operation. When this is unset, there is no ModifyVolume operation being attempted. This is an alpha field and requires enabling VolumeAttributesClass feature.
    """
    phase: NotRequired[Input[str]]
    """
    phase represents the current phase of PersistentVolumeClaim.
    """
    resize_status: NotRequired[Input[str]]
    """
    resizeStatus stores status of resize operation. ResizeStatus is not set by default but when expansion is complete resizeStatus is set to empty string by resize controller or kubelet. This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.
    """

class PersistentVolumeClaimTemplatePatchArgsDict(TypedDict):
    """
    PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource.
    """
    metadata: NotRequired[Input['ObjectMetaPatchArgsDict']]
    """
    May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation.
    """
    spec: NotRequired[Input['PersistentVolumeClaimSpecPatchArgsDict']]
    """
    The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here.
    """

class PersistentVolumeClaimTemplateArgsDict(TypedDict):
    """
    PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource.
    """
    spec: Input['PersistentVolumeClaimSpecArgsDict']
    """
    The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here.
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation.
    """

class PersistentVolumeClaimVolumeSourcePatchArgsDict(TypedDict):
    """
    PersistentVolumeClaimVolumeSource references the user's PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system).
    """
    claim_name: NotRequired[Input[str]]
    """
    claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly Will force the ReadOnly setting in VolumeMounts. Default false.
    """

class PersistentVolumeClaimVolumeSourceArgsDict(TypedDict):
    """
    PersistentVolumeClaimVolumeSource references the user's PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system).
    """
    claim_name: Input[str]
    """
    claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly Will force the ReadOnly setting in VolumeMounts. Default false.
    """

class PersistentVolumeClaimArgsDict(TypedDict):
    """
    PersistentVolumeClaim is a user's request for and claim to a persistent volume
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['PersistentVolumeClaimSpecArgsDict']]
    """
    spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    status: NotRequired[Input['PersistentVolumeClaimStatusArgsDict']]
    """
    status represents the current information/status of a persistent volume claim. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """

class PersistentVolumeSpecPatchArgsDict(TypedDict):
    """
    PersistentVolumeSpec is the specification of a persistent volume.
    """
    access_modes: NotRequired[Input[Sequence[Input[str]]]]
    """
    accessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
    """
    aws_elastic_block_store: NotRequired[Input['AWSElasticBlockStoreVolumeSourcePatchArgsDict']]
    """
    awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    azure_disk: NotRequired[Input['AzureDiskVolumeSourcePatchArgsDict']]
    """
    azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    """
    azure_file: NotRequired[Input['AzureFilePersistentVolumeSourcePatchArgsDict']]
    """
    azureFile represents an Azure File Service mount on the host and bind mount to the pod.
    """
    capacity: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    capacity is the description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity
    """
    cephfs: NotRequired[Input['CephFSPersistentVolumeSourcePatchArgsDict']]
    """
    cephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    """
    cinder: NotRequired[Input['CinderPersistentVolumeSourcePatchArgsDict']]
    """
    cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    claim_ref: NotRequired[Input['ObjectReferencePatchArgsDict']]
    """
    claimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
    """
    csi: NotRequired[Input['CSIPersistentVolumeSourcePatchArgsDict']]
    """
    csi represents storage that is handled by an external CSI driver (Beta feature).
    """
    fc: NotRequired[Input['FCVolumeSourcePatchArgsDict']]
    """
    fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    """
    flex_volume: NotRequired[Input['FlexPersistentVolumeSourcePatchArgsDict']]
    """
    flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    """
    flocker: NotRequired[Input['FlockerVolumeSourcePatchArgsDict']]
    """
    flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running
    """
    gce_persistent_disk: NotRequired[Input['GCEPersistentDiskVolumeSourcePatchArgsDict']]
    """
    gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    glusterfs: NotRequired[Input['GlusterfsPersistentVolumeSourcePatchArgsDict']]
    """
    glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    """
    host_path: NotRequired[Input['HostPathVolumeSourcePatchArgsDict']]
    """
    hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    iscsi: NotRequired[Input['ISCSIPersistentVolumeSourcePatchArgsDict']]
    """
    iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.
    """
    local: NotRequired[Input['LocalVolumeSourcePatchArgsDict']]
    """
    local represents directly-attached storage with node affinity
    """
    mount_options: NotRequired[Input[Sequence[Input[str]]]]
    """
    mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
    """
    nfs: NotRequired[Input['NFSVolumeSourcePatchArgsDict']]
    """
    nfs represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    node_affinity: NotRequired[Input['VolumeNodeAffinityPatchArgsDict']]
    """
    nodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.
    """
    persistent_volume_reclaim_policy: NotRequired[Input[str]]
    """
    persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
    """
    photon_persistent_disk: NotRequired[Input['PhotonPersistentDiskVolumeSourcePatchArgsDict']]
    """
    photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    """
    portworx_volume: NotRequired[Input['PortworxVolumeSourcePatchArgsDict']]
    """
    portworxVolume represents a portworx volume attached and mounted on kubelets host machine
    """
    quobyte: NotRequired[Input['QuobyteVolumeSourcePatchArgsDict']]
    """
    quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    """
    rbd: NotRequired[Input['RBDPersistentVolumeSourcePatchArgsDict']]
    """
    rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    """
    scale_io: NotRequired[Input['ScaleIOPersistentVolumeSourcePatchArgsDict']]
    """
    scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    """
    storage_class_name: NotRequired[Input[str]]
    """
    storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.
    """
    storageos: NotRequired[Input['StorageOSPersistentVolumeSourcePatchArgsDict']]
    """
    storageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md
    """
    volume_attributes_class_name: NotRequired[Input[str]]
    """
    Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process. This is an alpha field and requires enabling VolumeAttributesClass feature.
    """
    volume_mode: NotRequired[Input[str]]
    """
    volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.
    """
    vsphere_volume: NotRequired[Input['VsphereVirtualDiskVolumeSourcePatchArgsDict']]
    """
    vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    """

class PersistentVolumeSpecArgsDict(TypedDict):
    """
    PersistentVolumeSpec is the specification of a persistent volume.
    """
    access_modes: NotRequired[Input[Sequence[Input[str]]]]
    """
    accessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes
    """
    aws_elastic_block_store: NotRequired[Input['AWSElasticBlockStoreVolumeSourceArgsDict']]
    """
    awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    azure_disk: NotRequired[Input['AzureDiskVolumeSourceArgsDict']]
    """
    azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    """
    azure_file: NotRequired[Input['AzureFilePersistentVolumeSourceArgsDict']]
    """
    azureFile represents an Azure File Service mount on the host and bind mount to the pod.
    """
    capacity: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    capacity is the description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity
    """
    cephfs: NotRequired[Input['CephFSPersistentVolumeSourceArgsDict']]
    """
    cephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    """
    cinder: NotRequired[Input['CinderPersistentVolumeSourceArgsDict']]
    """
    cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    claim_ref: NotRequired[Input['ObjectReferenceArgsDict']]
    """
    claimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding
    """
    csi: NotRequired[Input['CSIPersistentVolumeSourceArgsDict']]
    """
    csi represents storage that is handled by an external CSI driver (Beta feature).
    """
    fc: NotRequired[Input['FCVolumeSourceArgsDict']]
    """
    fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    """
    flex_volume: NotRequired[Input['FlexPersistentVolumeSourceArgsDict']]
    """
    flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    """
    flocker: NotRequired[Input['FlockerVolumeSourceArgsDict']]
    """
    flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running
    """
    gce_persistent_disk: NotRequired[Input['GCEPersistentDiskVolumeSourceArgsDict']]
    """
    gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    glusterfs: NotRequired[Input['GlusterfsPersistentVolumeSourceArgsDict']]
    """
    glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    """
    host_path: NotRequired[Input['HostPathVolumeSourceArgsDict']]
    """
    hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    iscsi: NotRequired[Input['ISCSIPersistentVolumeSourceArgsDict']]
    """
    iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.
    """
    local: NotRequired[Input['LocalVolumeSourceArgsDict']]
    """
    local represents directly-attached storage with node affinity
    """
    mount_options: NotRequired[Input[Sequence[Input[str]]]]
    """
    mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options
    """
    nfs: NotRequired[Input['NFSVolumeSourceArgsDict']]
    """
    nfs represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    node_affinity: NotRequired[Input['VolumeNodeAffinityArgsDict']]
    """
    nodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.
    """
    persistent_volume_reclaim_policy: NotRequired[Input[str]]
    """
    persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming
    """
    photon_persistent_disk: NotRequired[Input['PhotonPersistentDiskVolumeSourceArgsDict']]
    """
    photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    """
    portworx_volume: NotRequired[Input['PortworxVolumeSourceArgsDict']]
    """
    portworxVolume represents a portworx volume attached and mounted on kubelets host machine
    """
    quobyte: NotRequired[Input['QuobyteVolumeSourceArgsDict']]
    """
    quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    """
    rbd: NotRequired[Input['RBDPersistentVolumeSourceArgsDict']]
    """
    rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    """
    scale_io: NotRequired[Input['ScaleIOPersistentVolumeSourceArgsDict']]
    """
    scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    """
    storage_class_name: NotRequired[Input[str]]
    """
    storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.
    """
    storageos: NotRequired[Input['StorageOSPersistentVolumeSourceArgsDict']]
    """
    storageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md
    """
    volume_attributes_class_name: NotRequired[Input[str]]
    """
    Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process. This is an alpha field and requires enabling VolumeAttributesClass feature.
    """
    volume_mode: NotRequired[Input[str]]
    """
    volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.
    """
    vsphere_volume: NotRequired[Input['VsphereVirtualDiskVolumeSourceArgsDict']]
    """
    vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    """

class PersistentVolumeStatusArgsDict(TypedDict):
    """
    PersistentVolumeStatus is the current status of a persistent volume.
    """
    last_phase_transition_time: NotRequired[Input[str]]
    """
    lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions. This is a beta field and requires the PersistentVolumeLastPhaseTransitionTime feature to be enabled (enabled by default).
    """
    message: NotRequired[Input[str]]
    """
    message is a human-readable message indicating details about why the volume is in this state.
    """
    phase: NotRequired[Input[str]]
    """
    phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase
    """
    reason: NotRequired[Input[str]]
    """
    reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.
    """

class PersistentVolumeArgsDict(TypedDict):
    """
    PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['PersistentVolumeSpecArgsDict']]
    """
    spec defines a specification of a persistent volume owned by the cluster. Provisioned by an administrator. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes
    """
    status: NotRequired[Input['PersistentVolumeStatusArgsDict']]
    """
    status represents the current information/status for the persistent volume. Populated by the system. Read-only. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes
    """

class PhotonPersistentDiskVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Photon Controller persistent disk resource.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    pd_id: NotRequired[Input[str]]
    """
    pdID is the ID that identifies Photon Controller persistent disk
    """

class PhotonPersistentDiskVolumeSourceArgsDict(TypedDict):
    """
    Represents a Photon Controller persistent disk resource.
    """
    pd_id: Input[str]
    """
    pdID is the ID that identifies Photon Controller persistent disk
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """

class PodAffinityPatchArgsDict(TypedDict):
    """
    Pod affinity is a group of inter pod affinity scheduling rules.
    """
    preferred_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['WeightedPodAffinityTermPatchArgsDict']]]]
    """
    The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    """
    required_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['PodAffinityTermPatchArgsDict']]]]
    """
    If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """

class PodAffinityTermPatchArgsDict(TypedDict):
    """
    Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    """
    label_selector: NotRequired[Input['LabelSelectorPatchArgsDict']]
    """
    A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
    """
    match_label_keys: NotRequired[Input[Sequence[Input[str]]]]
    """
    MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate.
    """
    mismatch_label_keys: NotRequired[Input[Sequence[Input[str]]]]
    """
    MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate.
    """
    namespace_selector: NotRequired[Input['LabelSelectorPatchArgsDict']]
    """
    A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.
    """
    namespaces: NotRequired[Input[Sequence[Input[str]]]]
    """
    namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
    """
    topology_key: NotRequired[Input[str]]
    """
    This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    """

class PodAffinityTermArgsDict(TypedDict):
    """
    Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    """
    topology_key: Input[str]
    """
    This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
    """
    label_selector: NotRequired[Input['LabelSelectorArgsDict']]
    """
    A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
    """
    match_label_keys: NotRequired[Input[Sequence[Input[str]]]]
    """
    MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate.
    """
    mismatch_label_keys: NotRequired[Input[Sequence[Input[str]]]]
    """
    MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate.
    """
    namespace_selector: NotRequired[Input['LabelSelectorArgsDict']]
    """
    A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.
    """
    namespaces: NotRequired[Input[Sequence[Input[str]]]]
    """
    namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
    """

class PodAffinityArgsDict(TypedDict):
    """
    Pod affinity is a group of inter pod affinity scheduling rules.
    """
    preferred_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['WeightedPodAffinityTermArgsDict']]]]
    """
    The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    """
    required_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['PodAffinityTermArgsDict']]]]
    """
    If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """

class PodAntiAffinityPatchArgsDict(TypedDict):
    """
    Pod anti affinity is a group of inter pod anti affinity scheduling rules.
    """
    preferred_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['WeightedPodAffinityTermPatchArgsDict']]]]
    """
    The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    """
    required_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['PodAffinityTermPatchArgsDict']]]]
    """
    If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """

class PodAntiAffinityArgsDict(TypedDict):
    """
    Pod anti affinity is a group of inter pod anti affinity scheduling rules.
    """
    preferred_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['WeightedPodAffinityTermArgsDict']]]]
    """
    The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
    """
    required_during_scheduling_ignored_during_execution: NotRequired[Input[Sequence[Input['PodAffinityTermArgsDict']]]]
    """
    If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.
    """

class PodConditionArgsDict(TypedDict):
    """
    PodCondition contains details for the current condition of this pod.
    """
    status: Input[str]
    """
    Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions
    """
    type: Input[str]
    """
    Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions
    """
    last_probe_time: NotRequired[Input[str]]
    """
    Last time we probed the condition.
    """
    last_transition_time: NotRequired[Input[str]]
    """
    Last time the condition transitioned from one status to another.
    """
    message: NotRequired[Input[str]]
    """
    Human-readable message indicating details about last transition.
    """
    reason: NotRequired[Input[str]]
    """
    Unique, one-word, CamelCase reason for the condition's last transition.
    """

class PodDNSConfigOptionPatchArgsDict(TypedDict):
    """
    PodDNSConfigOption defines DNS resolver options of a pod.
    """
    name: NotRequired[Input[str]]
    """
    Required.
    """
    value: NotRequired[Input[str]]

class PodDNSConfigOptionArgsDict(TypedDict):
    """
    PodDNSConfigOption defines DNS resolver options of a pod.
    """
    name: NotRequired[Input[str]]
    """
    Required.
    """
    value: NotRequired[Input[str]]

class PodDNSConfigPatchArgsDict(TypedDict):
    """
    PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.
    """
    nameservers: NotRequired[Input[Sequence[Input[str]]]]
    """
    A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.
    """
    options: NotRequired[Input[Sequence[Input['PodDNSConfigOptionPatchArgsDict']]]]
    """
    A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.
    """
    searches: NotRequired[Input[Sequence[Input[str]]]]
    """
    A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.
    """

class PodDNSConfigArgsDict(TypedDict):
    """
    PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.
    """
    nameservers: NotRequired[Input[Sequence[Input[str]]]]
    """
    A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.
    """
    options: NotRequired[Input[Sequence[Input['PodDNSConfigOptionArgsDict']]]]
    """
    A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.
    """
    searches: NotRequired[Input[Sequence[Input[str]]]]
    """
    A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.
    """

class PodIPArgsDict(TypedDict):
    """
    PodIP represents a single IP address allocated to the pod.
    """
    ip: NotRequired[Input[str]]
    """
    IP is the IP address assigned to the pod
    """

class PodOSPatchArgsDict(TypedDict):
    """
    PodOS defines the OS parameters of a pod.
    """
    name: NotRequired[Input[str]]
    """
    Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration Clients should expect to handle additional values and treat unrecognized values in this field as os: null
    """

class PodOSArgsDict(TypedDict):
    """
    PodOS defines the OS parameters of a pod.
    """
    name: Input[str]
    """
    Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration Clients should expect to handle additional values and treat unrecognized values in this field as os: null
    """

class PodReadinessGatePatchArgsDict(TypedDict):
    """
    PodReadinessGate contains the reference to a pod condition
    """
    condition_type: NotRequired[Input[str]]
    """
    ConditionType refers to a condition in the pod's condition list with matching type.
    """

class PodReadinessGateArgsDict(TypedDict):
    """
    PodReadinessGate contains the reference to a pod condition
    """
    condition_type: Input[str]
    """
    ConditionType refers to a condition in the pod's condition list with matching type.
    """

class PodResourceClaimPatchArgsDict(TypedDict):
    """
    PodResourceClaim references exactly one ResourceClaim through a ClaimSource. It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.
    """
    name: NotRequired[Input[str]]
    """
    Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL.
    """
    source: NotRequired[Input['ClaimSourcePatchArgsDict']]
    """
    Source describes where to find the ResourceClaim.
    """

class PodResourceClaimStatusArgsDict(TypedDict):
    """
    PodResourceClaimStatus is stored in the PodStatus for each PodResourceClaim which references a ResourceClaimTemplate. It stores the generated name for the corresponding ResourceClaim.
    """
    name: Input[str]
    """
    Name uniquely identifies this resource claim inside the pod. This must match the name of an entry in pod.spec.resourceClaims, which implies that the string must be a DNS_LABEL.
    """
    resource_claim_name: NotRequired[Input[str]]
    """
    ResourceClaimName is the name of the ResourceClaim that was generated for the Pod in the namespace of the Pod. It this is unset, then generating a ResourceClaim was not necessary. The pod.spec.resourceClaims entry can be ignored in this case.
    """

class PodResourceClaimArgsDict(TypedDict):
    """
    PodResourceClaim references exactly one ResourceClaim through a ClaimSource. It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.
    """
    name: Input[str]
    """
    Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL.
    """
    source: NotRequired[Input['ClaimSourceArgsDict']]
    """
    Source describes where to find the ResourceClaim.
    """

class PodSchedulingGatePatchArgsDict(TypedDict):
    """
    PodSchedulingGate is associated to a Pod to guard its scheduling.
    """
    name: NotRequired[Input[str]]
    """
    Name of the scheduling gate. Each scheduling gate must have a unique name field.
    """

class PodSchedulingGateArgsDict(TypedDict):
    """
    PodSchedulingGate is associated to a Pod to guard its scheduling.
    """
    name: Input[str]
    """
    Name of the scheduling gate. Each scheduling gate must have a unique name field.
    """

class PodSecurityContextPatchArgsDict(TypedDict):
    """
    PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext.  Field values of container.securityContext take precedence over field values of PodSecurityContext.
    """
    app_armor_profile: NotRequired[Input['AppArmorProfilePatchArgsDict']]
    """
    appArmorProfile is the AppArmor options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.
    """
    fs_group: NotRequired[Input[int]]
    """
    A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:

    1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----

    If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.
    """
    fs_group_change_policy: NotRequired[Input[str]]
    """
    fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows.
    """
    run_as_group: NotRequired[Input[int]]
    """
    The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
    """
    run_as_non_root: NotRequired[Input[bool]]
    """
    Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    run_as_user: NotRequired[Input[int]]
    """
    The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
    """
    se_linux_options: NotRequired[Input['SELinuxOptionsPatchArgsDict']]
    """
    The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
    """
    seccomp_profile: NotRequired[Input['SeccompProfilePatchArgsDict']]
    """
    The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.
    """
    supplemental_groups: NotRequired[Input[Sequence[Input[int]]]]
    """
    A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows.
    """
    sysctls: NotRequired[Input[Sequence[Input['SysctlPatchArgsDict']]]]
    """
    Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.
    """
    windows_options: NotRequired[Input['WindowsSecurityContextOptionsPatchArgsDict']]
    """
    The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.
    """

class PodSecurityContextArgsDict(TypedDict):
    """
    PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext.  Field values of container.securityContext take precedence over field values of PodSecurityContext.
    """
    app_armor_profile: NotRequired[Input['AppArmorProfileArgsDict']]
    """
    appArmorProfile is the AppArmor options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.
    """
    fs_group: NotRequired[Input[int]]
    """
    A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:

    1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----

    If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.
    """
    fs_group_change_policy: NotRequired[Input[str]]
    """
    fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows.
    """
    run_as_group: NotRequired[Input[int]]
    """
    The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
    """
    run_as_non_root: NotRequired[Input[bool]]
    """
    Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    run_as_user: NotRequired[Input[int]]
    """
    The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
    """
    se_linux_options: NotRequired[Input['SELinuxOptionsArgsDict']]
    """
    The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
    """
    seccomp_profile: NotRequired[Input['SeccompProfileArgsDict']]
    """
    The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.
    """
    supplemental_groups: NotRequired[Input[Sequence[Input[int]]]]
    """
    A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows.
    """
    sysctls: NotRequired[Input[Sequence[Input['SysctlArgsDict']]]]
    """
    Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.
    """
    windows_options: NotRequired[Input['WindowsSecurityContextOptionsArgsDict']]
    """
    The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.
    """

class PodSpecPatchArgsDict(TypedDict):
    """
    PodSpec is a description of a pod.
    """
    active_deadline_seconds: NotRequired[Input[int]]
    """
    Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.
    """
    affinity: NotRequired[Input['AffinityPatchArgsDict']]
    """
    If specified, the pod's scheduling constraints
    """
    automount_service_account_token: NotRequired[Input[bool]]
    """
    AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.
    """
    containers: NotRequired[Input[Sequence[Input['ContainerPatchArgsDict']]]]
    """
    List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.
    """
    dns_config: NotRequired[Input['PodDNSConfigPatchArgsDict']]
    """
    Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.
    """
    dns_policy: NotRequired[Input[str]]
    """
    Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.
    """
    enable_service_links: NotRequired[Input[bool]]
    """
    EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.
    """
    ephemeral_containers: NotRequired[Input[Sequence[Input['EphemeralContainerPatchArgsDict']]]]
    """
    List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource.
    """
    host_aliases: NotRequired[Input[Sequence[Input['HostAliasPatchArgsDict']]]]
    """
    HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified.
    """
    host_ipc: NotRequired[Input[bool]]
    """
    Use the host's ipc namespace. Optional: Default to false.
    """
    host_network: NotRequired[Input[bool]]
    """
    Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.
    """
    host_pid: NotRequired[Input[bool]]
    """
    Use the host's pid namespace. Optional: Default to false.
    """
    host_users: NotRequired[Input[bool]]
    """
    Use the host's user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature.
    """
    hostname: NotRequired[Input[str]]
    """
    Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.
    """
    image_pull_secrets: NotRequired[Input[Sequence[Input['LocalObjectReferencePatchArgsDict']]]]
    """
    ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod
    """
    init_containers: NotRequired[Input[Sequence[Input['ContainerPatchArgsDict']]]]
    """
    List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
    """
    node_name: NotRequired[Input[str]]
    """
    NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.
    """
    node_selector: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
    """
    os: NotRequired[Input['PodOSPatchArgsDict']]
    """
    Specifies the OS of the containers in the pod. Some pod and container fields are restricted if this is set.

    If the OS field is set to linux, the following fields must be unset: -securityContext.windowsOptions

    If the OS field is set to windows, following fields must be unset: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.securityContext.appArmorProfile - spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile - spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy - spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser - spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups - spec.containers[*].securityContext.appArmorProfile - spec.containers[*].securityContext.seLinuxOptions - spec.containers[*].securityContext.seccompProfile - spec.containers[*].securityContext.capabilities - spec.containers[*].securityContext.readOnlyRootFilesystem - spec.containers[*].securityContext.privileged - spec.containers[*].securityContext.allowPrivilegeEscalation - spec.containers[*].securityContext.procMount - spec.containers[*].securityContext.runAsUser - spec.containers[*].securityContext.runAsGroup
    """
    overhead: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md
    """
    preemption_policy: NotRequired[Input[str]]
    """
    PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.
    """
    priority: NotRequired[Input[int]]
    """
    The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.
    """
    priority_class_name: NotRequired[Input[str]]
    """
    If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.
    """
    readiness_gates: NotRequired[Input[Sequence[Input['PodReadinessGatePatchArgsDict']]]]
    """
    If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates
    """
    resource_claims: NotRequired[Input[Sequence[Input['PodResourceClaimPatchArgsDict']]]]
    """
    ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.

    This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

    This field is immutable.
    """
    restart_policy: NotRequired[Input[str]]
    """
    Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
    """
    runtime_class_name: NotRequired[Input[str]]
    """
    RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class
    """
    scheduler_name: NotRequired[Input[str]]
    """
    If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.
    """
    scheduling_gates: NotRequired[Input[Sequence[Input['PodSchedulingGatePatchArgsDict']]]]
    """
    SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.

    SchedulingGates can only be set at pod creation time, and be removed only afterwards.
    """
    security_context: NotRequired[Input['PodSecurityContextPatchArgsDict']]
    """
    SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.
    """
    service_account: NotRequired[Input[str]]
    """
    DeprecatedServiceAccount is a deprecated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.
    """
    service_account_name: NotRequired[Input[str]]
    """
    ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
    """
    set_hostname_as_fqdn: NotRequired[Input[bool]]
    """
    If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false.
    """
    share_process_namespace: NotRequired[Input[bool]]
    """
    Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.
    """
    subdomain: NotRequired[Input[str]]
    """
    If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.
    """
    termination_grace_period_seconds: NotRequired[Input[int]]
    """
    Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.
    """
    tolerations: NotRequired[Input[Sequence[Input['TolerationPatchArgsDict']]]]
    """
    If specified, the pod's tolerations.
    """
    topology_spread_constraints: NotRequired[Input[Sequence[Input['TopologySpreadConstraintPatchArgsDict']]]]
    """
    TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.
    """
    volumes: NotRequired[Input[Sequence[Input['VolumePatchArgsDict']]]]
    """
    List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes
    """

class PodSpecArgsDict(TypedDict):
    """
    PodSpec is a description of a pod.
    """
    containers: Input[Sequence[Input['ContainerArgsDict']]]
    """
    List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.
    """
    active_deadline_seconds: NotRequired[Input[int]]
    """
    Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.
    """
    affinity: NotRequired[Input['AffinityArgsDict']]
    """
    If specified, the pod's scheduling constraints
    """
    automount_service_account_token: NotRequired[bool]
    """
    AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.
    """
    dns_config: NotRequired[Input['PodDNSConfigArgsDict']]
    """
    Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.
    """
    dns_policy: NotRequired[Input[str]]
    """
    Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.
    """
    enable_service_links: NotRequired[Input[bool]]
    """
    EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.
    """
    ephemeral_containers: NotRequired[Input[Sequence[Input['EphemeralContainerArgsDict']]]]
    """
    List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource.
    """
    host_aliases: NotRequired[Input[Sequence[Input['HostAliasArgsDict']]]]
    """
    HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified.
    """
    host_ipc: NotRequired[Input[bool]]
    """
    Use the host's ipc namespace. Optional: Default to false.
    """
    host_network: NotRequired[Input[bool]]
    """
    Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.
    """
    host_pid: NotRequired[Input[bool]]
    """
    Use the host's pid namespace. Optional: Default to false.
    """
    host_users: NotRequired[Input[bool]]
    """
    Use the host's user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature.
    """
    # hostname: NotRequired[Input[str]]
    # """
    # Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.
    # """
    # image_pull_secrets: NotRequired[Input[Sequence[Input['LocalObjectReferenceArgsDict']]]]
    # """
    # ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod
    # """
    # init_containers: NotRequired[Input[Sequence[Input['ContainerArgsDict']]]]
    # """
    # List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
    # """
    # node_name: NotRequired[Input[str]]
    # """
    # NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.
    # """
    # node_selector: NotRequired[Input[Mapping[str, Input[str]]]]
    # """
    # NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
    # """
    # os: NotRequired[Input['PodOSArgsDict']]
    # """
    # Specifies the OS of the containers in the pod. Some pod and container fields are restricted if this is set.

    # If the OS field is set to linux, the following fields must be unset: -securityContext.windowsOptions

    # If the OS field is set to windows, following fields must be unset: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.securityContext.appArmorProfile - spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile - spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy - spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser - spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups - spec.containers[*].securityContext.appArmorProfile - spec.containers[*].securityContext.seLinuxOptions - spec.containers[*].securityContext.seccompProfile - spec.containers[*].securityContext.capabilities - spec.containers[*].securityContext.readOnlyRootFilesystem - spec.containers[*].securityContext.privileged - spec.containers[*].securityContext.allowPrivilegeEscalation - spec.containers[*].securityContext.procMount - spec.containers[*].securityContext.runAsUser - spec.containers[*].securityContext.runAsGroup
    # """
    # overhead: NotRequired[Input[Mapping[str, Input[str]]]]
    # """
    # Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md
    # """
    # preemption_policy: NotRequired[Input[str]]
    # """
    # PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.
    # """
    # priority: NotRequired[Input[int]]
    # """
    # The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.
    # """
    # priority_class_name: NotRequired[Input[str]]
    # """
    # If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.
    # """
    # readiness_gates: NotRequired[Input[Sequence[Input['PodReadinessGateArgsDict']]]]
    # """
    # If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates
    # """
    # resource_claims: NotRequired[Input[Sequence[Input['PodResourceClaimArgsDict']]]]
    # """
    # ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.

    # This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

    # This field is immutable.
    # """
    # restart_policy: NotRequired[Input[str]]
    # """
    # Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy
    # """
    # runtime_class_name: NotRequired[Input[str]]
    # """
    # RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class
    # """
    # scheduler_name: NotRequired[Input[str]]
    # """
    # If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.
    # """
    # scheduling_gates: NotRequired[Input[Sequence[Input['PodSchedulingGateArgsDict']]]]
    # """
    # SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.

    # SchedulingGates can only be set at pod creation time, and be removed only afterwards.
    # """
    # security_context: NotRequired[Input['PodSecurityContextArgsDict']]
    # """
    # SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.
    # """
    # service_account: NotRequired[Input[str]]
    # """
    # DeprecatedServiceAccount is a deprecated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.
    # """
    # service_account_name: NotRequired[Input[str]]
    # """
    # ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
    # """
    # set_hostname_as_fqdn: NotRequired[Input[bool]]
    # """
    # If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false.
    # """
    # share_process_namespace: NotRequired[Input[bool]]
    # """
    # Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.
    # """
    # subdomain: NotRequired[Input[str]]
    # """
    # If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.
    # """
    # termination_grace_period_seconds: NotRequired[Input[int]]
    # """
    # Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.
    # """
    # tolerations: NotRequired[Input[Sequence[Input['TolerationArgsDict']]]]
    # """
    # If specified, the pod's tolerations.
    # """
    # topology_spread_constraints: NotRequired[Input[Sequence[Input['TopologySpreadConstraintArgsDict']]]]
    # """
    # TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.
    # """
    # volumes: NotRequired[Input[Sequence[Input['VolumeArgsDict']]]]
    # """
    # List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes
    # """

class PodStatusArgsDict(TypedDict):
    """
    PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane.
    """
    conditions: NotRequired[Input[Sequence[Input['PodConditionArgsDict']]]]
    """
    Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions
    """
    container_statuses: NotRequired[Input[Sequence[Input['ContainerStatusArgsDict']]]]
    """
    The list has one entry per container in the manifest. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status
    """
    ephemeral_container_statuses: NotRequired[Input[Sequence[Input['ContainerStatusArgsDict']]]]
    """
    Status for any ephemeral containers that have run in this pod.
    """
    host_ip: NotRequired[Input[str]]
    """
    hostIP holds the IP address of the host to which the pod is assigned. Empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns mean that HostIP will not be updated even if there is a node is assigned to pod
    """
    host_ips: NotRequired[Input[Sequence[Input['HostIPArgsDict']]]]
    """
    hostIPs holds the IP addresses allocated to the host. If this field is specified, the first entry must match the hostIP field. This list is empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns means that HostIPs will not be updated even if there is a node is assigned to this pod.
    """
    init_container_statuses: NotRequired[Input[Sequence[Input['ContainerStatusArgsDict']]]]
    """
    The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status
    """
    message: NotRequired[Input[str]]
    """
    A human readable message indicating details about why the pod is in this condition.
    """
    nominated_node_name: NotRequired[Input[str]]
    """
    nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.
    """
    phase: NotRequired[Input[str]]
    """
    The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:

    Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.

    More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase
    """
    pod_ip: NotRequired[Input[str]]
    """
    podIP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.
    """
    pod_ips: NotRequired[Input[Sequence[Input['PodIPArgsDict']]]]
    """
    podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet.
    """
    qos_class: NotRequired[Input[str]]
    """
    The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#quality-of-service-classes
    """
    reason: NotRequired[Input[str]]
    """
    A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'
    """
    resize: NotRequired[Input[str]]
    """
    Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to "Proposed"
    """
    resource_claim_statuses: NotRequired[Input[Sequence[Input['PodResourceClaimStatusArgsDict']]]]
    """
    Status of resource claims.
    """
    start_time: NotRequired[Input[str]]
    """
    RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.
    """

class PodTemplateSpecPatchArgsDict(TypedDict):
    """
    PodTemplateSpec describes the data a pod should have when created from a template
    """
    metadata: NotRequired[Input['ObjectMetaPatchArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['PodSpecPatchArgsDict']]
    """
    Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class PodTemplateSpecArgsDict(TypedDict):
    """
    PodTemplateSpec describes the data a pod should have when created from a template
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['PodSpecArgsDict']]
    """
    Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class PodTemplateArgsDict(TypedDict):
    """
    PodTemplate describes a template for creating copies of a predefined pod.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    template: NotRequired[Input['PodTemplateSpecArgsDict']]
    """
    Template defines the pods that will be created from this pod template. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class PodArgsDict(TypedDict):
    """
    Pod is a collection of containers that can run on a host. This resource is created by clients and scheduled onto hosts.

    This resource waits until its status is ready before registering success
    for create/update, and populating output properties from the current state of the resource.
    The following conditions are used to determine whether the resource creation has
    succeeded or failed:

    1. The Pod is scheduled ("PodScheduled"" '.status.condition' is true).
    2. The Pod is initialized ("Initialized" '.status.condition' is true).
    3. The Pod is ready ("Ready" '.status.condition' is true) and the '.status.phase' is
       set to "Running".
    Or (for Jobs): The Pod succeeded ('.status.phase' set to "Succeeded").

    If the Pod has not reached a Ready state after 10 minutes, it will
    time out and mark the resource update as Failed. You can override the default timeout value
    by setting the 'customTimeouts' option on the resource.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['PodSpecArgsDict']]
    """
    Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    status: NotRequired[Input['PodStatusArgsDict']]
    """
    Most recently observed status of the pod. This data may not be up to date. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class PortStatusArgsDict(TypedDict):
    port: Input[int]
    """
    Port is the port number of the service port of which status is recorded here
    """
    protocol: Input[str]
    """
    Protocol is the protocol of the service port of which status is recorded here The supported values are: "TCP", "UDP", "SCTP"
    """
    error: NotRequired[Input[str]]
    """
    Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use
      CamelCase names
    - cloud provider specific error values must have names that comply with the
      format foo.example.com/CamelCase.
    """

class PortworxVolumeSourcePatchArgsDict(TypedDict):
    """
    PortworxVolumeSource represents a Portworx volume resource.
    """
    fs_type: NotRequired[Input[str]]
    """
    fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    volume_id: NotRequired[Input[str]]
    """
    volumeID uniquely identifies a Portworx volume
    """

class PortworxVolumeSourceArgsDict(TypedDict):
    """
    PortworxVolumeSource represents a Portworx volume resource.
    """
    volume_id: Input[str]
    """
    volumeID uniquely identifies a Portworx volume
    """
    fs_type: NotRequired[Input[str]]
    """
    fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """

class PreferredSchedulingTermPatchArgsDict(TypedDict):
    """
    An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).
    """
    preference: NotRequired[Input['NodeSelectorTermPatchArgsDict']]
    """
    A node selector term, associated with the corresponding weight.
    """
    weight: NotRequired[Input[int]]
    """
    Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.
    """

class PreferredSchedulingTermArgsDict(TypedDict):
    """
    An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).
    """
    preference: Input['NodeSelectorTermArgsDict']
    """
    A node selector term, associated with the corresponding weight.
    """
    weight: Input[int]
    """
    Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.
    """

class ProbePatchArgsDict(TypedDict):
    """
    Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.
    """
    exec_: NotRequired[Input['ExecActionPatchArgsDict']]
    """
    Exec specifies the action to take.
    """
    failure_threshold: NotRequired[Input[int]]
    """
    Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    """
    grpc: NotRequired[Input['GRPCActionPatchArgsDict']]
    """
    GRPC specifies an action involving a GRPC port.
    """
    http_get: NotRequired[Input['HTTPGetActionPatchArgsDict']]
    """
    HTTPGet specifies the http request to perform.
    """
    initial_delay_seconds: NotRequired[Input[int]]
    """
    Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    period_seconds: NotRequired[Input[int]]
    """
    How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    """
    success_threshold: NotRequired[Input[int]]
    """
    Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    """
    tcp_socket: NotRequired[Input['TCPSocketActionPatchArgsDict']]
    """
    TCPSocket specifies an action involving a TCP port.
    """
    termination_grace_period_seconds: NotRequired[Input[int]]
    """
    Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.
    """
    timeout_seconds: NotRequired[Input[int]]
    """
    Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """

class ProbeArgsDict(TypedDict):
    """
    Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.
    """
    exec_: NotRequired[Input['ExecActionArgsDict']]
    """
    Exec specifies the action to take.
    """
    failure_threshold: NotRequired[Input[int]]
    """
    Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.
    """
    grpc: NotRequired[Input['GRPCActionArgsDict']]
    """
    GRPC specifies an action involving a GRPC port.
    """
    http_get: NotRequired[Input['HTTPGetActionArgsDict']]
    """
    HTTPGet specifies the http request to perform.
    """
    initial_delay_seconds: NotRequired[Input[int]]
    """
    Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """
    period_seconds: NotRequired[Input[int]]
    """
    How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
    """
    success_threshold: NotRequired[Input[int]]
    """
    Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
    """
    tcp_socket: NotRequired[Input['TCPSocketActionArgsDict']]
    """
    TCPSocket specifies an action involving a TCP port.
    """
    termination_grace_period_seconds: NotRequired[Input[int]]
    """
    Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.
    """
    timeout_seconds: NotRequired[Input[int]]
    """
    Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """

class ProjectedVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a projected volume source
    """
    default_mode: NotRequired[Input[int]]
    """
    defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    sources: NotRequired[Input[Sequence[Input['VolumeProjectionPatchArgsDict']]]]
    """
    sources is the list of volume projections
    """

class ProjectedVolumeSourceArgsDict(TypedDict):
    """
    Represents a projected volume source
    """
    sources: Input[Sequence[Input['VolumeProjectionArgsDict']]]
    """
    sources is the list of volume projections
    """
    default_mode: NotRequired[Input[int]]
    """
    defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """

class QuobyteVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling.
    """
    group: NotRequired[Input[str]]
    """
    group to map volume access to Default is no group
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.
    """
    registry: NotRequired[Input[str]]
    """
    registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes
    """
    tenant: NotRequired[Input[str]]
    """
    tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin
    """
    user: NotRequired[Input[str]]
    """
    user to map volume access to Defaults to serivceaccount user
    """
    volume: NotRequired[Input[str]]
    """
    volume is a string that references an already created Quobyte volume by name.
    """

class QuobyteVolumeSourceArgsDict(TypedDict):
    """
    Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling.
    """
    registry: Input[str]
    """
    registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes
    """
    volume: Input[str]
    """
    volume is a string that references an already created Quobyte volume by name.
    """
    group: NotRequired[Input[str]]
    """
    group to map volume access to Default is no group
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.
    """
    tenant: NotRequired[Input[str]]
    """
    tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin
    """
    user: NotRequired[Input[str]]
    """
    user to map volume access to Defaults to serivceaccount user
    """

class RBDPersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd
    """
    image: NotRequired[Input[str]]
    """
    image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    keyring: NotRequired[Input[str]]
    """
    keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    monitors: NotRequired[Input[Sequence[Input[str]]]]
    """
    monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    pool: NotRequired[Input[str]]
    """
    pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    user: NotRequired[Input[str]]
    """
    user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """

class RBDPersistentVolumeSourceArgsDict(TypedDict):
    """
    Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.
    """
    image: Input[str]
    """
    image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    monitors: Input[Sequence[Input[str]]]
    """
    monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd
    """
    keyring: NotRequired[Input[str]]
    """
    keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    pool: NotRequired[Input[str]]
    """
    pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    secret_ref: NotRequired[Input['SecretReferenceArgsDict']]
    """
    secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    user: NotRequired[Input[str]]
    """
    user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """

class RBDVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd
    """
    image: NotRequired[Input[str]]
    """
    image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    keyring: NotRequired[Input[str]]
    """
    keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    monitors: NotRequired[Input[Sequence[Input[str]]]]
    """
    monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    pool: NotRequired[Input[str]]
    """
    pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    secret_ref: NotRequired[Input['LocalObjectReferencePatchArgsDict']]
    """
    secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    user: NotRequired[Input[str]]
    """
    user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """

class RBDVolumeSourceArgsDict(TypedDict):
    """
    Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.
    """
    image: Input[str]
    """
    image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    monitors: Input[Sequence[Input[str]]]
    """
    monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd
    """
    keyring: NotRequired[Input[str]]
    """
    keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    pool: NotRequired[Input[str]]
    """
    pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    secret_ref: NotRequired[Input['LocalObjectReferenceArgsDict']]
    """
    secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """
    user: NotRequired[Input[str]]
    """
    user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it
    """

class ReplicationControllerConditionArgsDict(TypedDict):
    """
    ReplicationControllerCondition describes the state of a replication controller at a certain point.
    """
    status: Input[str]
    """
    Status of the condition, one of True, False, Unknown.
    """
    type: Input[str]
    """
    Type of replication controller condition.
    """
    last_transition_time: NotRequired[Input[str]]
    """
    The last time the condition transitioned from one status to another.
    """
    message: NotRequired[Input[str]]
    """
    A human readable message indicating details about the transition.
    """
    reason: NotRequired[Input[str]]
    """
    The reason for the condition's last transition.
    """

class ReplicationControllerSpecPatchArgsDict(TypedDict):
    """
    ReplicationControllerSpec is the specification of a replication controller.
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    """
    replicas: NotRequired[Input[int]]
    """
    Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller
    """
    selector: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    """
    template: NotRequired[Input['PodTemplateSpecPatchArgsDict']]
    """
    Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template
    """

class ReplicationControllerSpecArgsDict(TypedDict):
    """
    ReplicationControllerSpec is the specification of a replication controller.
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    """
    replicas: NotRequired[Input[int]]
    """
    Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller
    """
    selector: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    """
    template: NotRequired[Input['PodTemplateSpecArgsDict']]
    """
    Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template
    """

class ReplicationControllerStatusArgsDict(TypedDict):
    """
    ReplicationControllerStatus represents the current status of a replication controller.
    """
    replicas: Input[int]
    """
    Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller
    """
    available_replicas: NotRequired[Input[int]]
    """
    The number of available replicas (ready for at least minReadySeconds) for this replication controller.
    """
    conditions: NotRequired[Input[Sequence[Input['ReplicationControllerConditionArgsDict']]]]
    """
    Represents the latest available observations of a replication controller's current state.
    """
    fully_labeled_replicas: NotRequired[Input[int]]
    """
    The number of pods that have labels matching the labels of the pod template of the replication controller.
    """
    observed_generation: NotRequired[Input[int]]
    """
    ObservedGeneration reflects the generation of the most recently observed replication controller.
    """
    ready_replicas: NotRequired[Input[int]]
    """
    The number of ready replicas for this replication controller.
    """

class ReplicationControllerArgsDict(TypedDict):
    """
    ReplicationController represents the configuration of a replication controller.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    If the Labels of a ReplicationController are empty, they are defaulted to be the same as the Pod(s) that the replication controller manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['ReplicationControllerSpecArgsDict']]
    """
    Spec defines the specification of the desired behavior of the replication controller. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    status: NotRequired[Input['ReplicationControllerStatusArgsDict']]
    """
    Status is the most recently observed status of the replication controller. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class ResourceClaimPatchArgsDict(TypedDict):
    """
    ResourceClaim references one entry in PodSpec.ResourceClaims.
    """
    name: NotRequired[Input[str]]
    """
    Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.
    """

class ResourceClaimArgsDict(TypedDict):
    """
    ResourceClaim references one entry in PodSpec.ResourceClaims.
    """
    name: Input[str]
    """
    Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.
    """

class ResourceFieldSelectorPatchArgsDict(TypedDict):
    """
    ResourceFieldSelector represents container resources (cpu, memory) and their output format
    """
    container_name: NotRequired[Input[str]]
    """
    Container name: required for volumes, optional for env vars
    """
    divisor: NotRequired[Input[str]]
    """
    Specifies the output format of the exposed resources, defaults to "1"
    """
    resource: NotRequired[Input[str]]
    """
    Required: resource to select
    """

class ResourceFieldSelectorArgsDict(TypedDict):
    """
    ResourceFieldSelector represents container resources (cpu, memory) and their output format
    """
    resource: Input[str]
    """
    Required: resource to select
    """
    container_name: NotRequired[Input[str]]
    """
    Container name: required for volumes, optional for env vars
    """
    divisor: NotRequired[Input[str]]
    """
    Specifies the output format of the exposed resources, defaults to "1"
    """

class ResourceQuotaSpecPatchArgsDict(TypedDict):
    """
    ResourceQuotaSpec defines the desired hard limits to enforce for Quota.
    """
    hard: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
    """
    scope_selector: NotRequired[Input['ScopeSelectorPatchArgsDict']]
    """
    scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched.
    """
    scopes: NotRequired[Input[Sequence[Input[str]]]]
    """
    A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.
    """

class ResourceQuotaSpecArgsDict(TypedDict):
    """
    ResourceQuotaSpec defines the desired hard limits to enforce for Quota.
    """
    hard: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
    """
    scope_selector: NotRequired[Input['ScopeSelectorArgsDict']]
    """
    scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched.
    """
    scopes: NotRequired[Input[Sequence[Input[str]]]]
    """
    A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.
    """

class ResourceQuotaStatusArgsDict(TypedDict):
    """
    ResourceQuotaStatus defines the enforced hard limits and observed use.
    """
    hard: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
    """
    used: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Used is the current observed total usage of the resource in the namespace.
    """

class ResourceQuotaArgsDict(TypedDict):
    """
    ResourceQuota sets aggregate quota restrictions enforced per namespace
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['ResourceQuotaSpecArgsDict']]
    """
    Spec defines the desired quota. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    status: NotRequired[Input['ResourceQuotaStatusArgsDict']]
    """
    Status defines the actual enforced quota and its current usage. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class ResourceRequirementsPatchArgsDict(TypedDict):
    """
    ResourceRequirements describes the compute resource requirements.
    """
    claims: NotRequired[Input[Sequence[Input['ResourceClaimPatchArgsDict']]]]
    """
    Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

    This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

    This field is immutable. It can only be set for containers.
    """
    limits: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """
    requests: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """

class ResourceRequirementsArgsDict(TypedDict):
    """
    ResourceRequirements describes the compute resource requirements.
    """
    claims: NotRequired[Input[Sequence[Input['ResourceClaimArgsDict']]]]
    """
    Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

    This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

    This field is immutable. It can only be set for containers.
    """
    limits: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """
    requests: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """

class SELinuxOptionsPatchArgsDict(TypedDict):
    """
    SELinuxOptions are the labels to be applied to the container
    """
    level: NotRequired[Input[str]]
    """
    Level is SELinux level label that applies to the container.
    """
    role: NotRequired[Input[str]]
    """
    Role is a SELinux role label that applies to the container.
    """
    type: NotRequired[Input[str]]
    """
    Type is a SELinux type label that applies to the container.
    """
    user: NotRequired[Input[str]]
    """
    User is a SELinux user label that applies to the container.
    """

class SELinuxOptionsArgsDict(TypedDict):
    """
    SELinuxOptions are the labels to be applied to the container
    """
    level: NotRequired[Input[str]]
    """
    Level is SELinux level label that applies to the container.
    """
    role: NotRequired[Input[str]]
    """
    Role is a SELinux role label that applies to the container.
    """
    type: NotRequired[Input[str]]
    """
    Type is a SELinux type label that applies to the container.
    """
    user: NotRequired[Input[str]]
    """
    User is a SELinux user label that applies to the container.
    """

class ScaleIOPersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs"
    """
    gateway: NotRequired[Input[str]]
    """
    gateway is the host address of the ScaleIO API Gateway.
    """
    protection_domain: NotRequired[Input[str]]
    """
    protectionDomain is the name of the ScaleIO Protection Domain for the configured storage.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['SecretReferencePatchArgsDict']]
    """
    secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    """
    ssl_enabled: NotRequired[Input[bool]]
    """
    sslEnabled is the flag to enable/disable SSL communication with Gateway, default false
    """
    storage_mode: NotRequired[Input[str]]
    """
    storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.
    """
    storage_pool: NotRequired[Input[str]]
    """
    storagePool is the ScaleIO Storage Pool associated with the protection domain.
    """
    system: NotRequired[Input[str]]
    """
    system is the name of the storage system as configured in ScaleIO.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source.
    """

class ScaleIOPersistentVolumeSourceArgsDict(TypedDict):
    """
    ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume
    """
    gateway: Input[str]
    """
    gateway is the host address of the ScaleIO API Gateway.
    """
    secret_ref: Input['SecretReferenceArgsDict']
    """
    secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    """
    system: Input[str]
    """
    system is the name of the storage system as configured in ScaleIO.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs"
    """
    protection_domain: NotRequired[Input[str]]
    """
    protectionDomain is the name of the ScaleIO Protection Domain for the configured storage.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    ssl_enabled: NotRequired[Input[bool]]
    """
    sslEnabled is the flag to enable/disable SSL communication with Gateway, default false
    """
    storage_mode: NotRequired[Input[str]]
    """
    storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.
    """
    storage_pool: NotRequired[Input[str]]
    """
    storagePool is the ScaleIO Storage Pool associated with the protection domain.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source.
    """

class ScaleIOVolumeSourcePatchArgsDict(TypedDict):
    """
    ScaleIOVolumeSource represents a persistent ScaleIO volume
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".
    """
    gateway: NotRequired[Input[str]]
    """
    gateway is the host address of the ScaleIO API Gateway.
    """
    protection_domain: NotRequired[Input[str]]
    """
    protectionDomain is the name of the ScaleIO Protection Domain for the configured storage.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['LocalObjectReferencePatchArgsDict']]
    """
    secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    """
    ssl_enabled: NotRequired[Input[bool]]
    """
    sslEnabled Flag enable/disable SSL communication with Gateway, default false
    """
    storage_mode: NotRequired[Input[str]]
    """
    storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.
    """
    storage_pool: NotRequired[Input[str]]
    """
    storagePool is the ScaleIO Storage Pool associated with the protection domain.
    """
    system: NotRequired[Input[str]]
    """
    system is the name of the storage system as configured in ScaleIO.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source.
    """

class ScaleIOVolumeSourceArgsDict(TypedDict):
    """
    ScaleIOVolumeSource represents a persistent ScaleIO volume
    """
    gateway: Input[str]
    """
    gateway is the host address of the ScaleIO API Gateway.
    """
    secret_ref: Input['LocalObjectReferenceArgsDict']
    """
    secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.
    """
    system: Input[str]
    """
    system is the name of the storage system as configured in ScaleIO.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".
    """
    protection_domain: NotRequired[Input[str]]
    """
    protectionDomain is the name of the ScaleIO Protection Domain for the configured storage.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    ssl_enabled: NotRequired[Input[bool]]
    """
    sslEnabled Flag enable/disable SSL communication with Gateway, default false
    """
    storage_mode: NotRequired[Input[str]]
    """
    storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.
    """
    storage_pool: NotRequired[Input[str]]
    """
    storagePool is the ScaleIO Storage Pool associated with the protection domain.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source.
    """

class ScopeSelectorPatchArgsDict(TypedDict):
    """
    A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements.
    """
    match_expressions: NotRequired[Input[Sequence[Input['ScopedResourceSelectorRequirementPatchArgsDict']]]]
    """
    A list of scope selector requirements by scope of the resources.
    """

class ScopeSelectorArgsDict(TypedDict):
    """
    A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements.
    """
    match_expressions: NotRequired[Input[Sequence[Input['ScopedResourceSelectorRequirementArgsDict']]]]
    """
    A list of scope selector requirements by scope of the resources.
    """

class ScopedResourceSelectorRequirementPatchArgsDict(TypedDict):
    """
    A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values.
    """
    operator: NotRequired[Input[str]]
    """
    Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.
    """
    scope_name: NotRequired[Input[str]]
    """
    The name of the scope that the selector applies to.
    """
    values: NotRequired[Input[Sequence[Input[str]]]]
    """
    An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """

class ScopedResourceSelectorRequirementArgsDict(TypedDict):
    """
    A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values.
    """
    operator: Input[str]
    """
    Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist.
    """
    scope_name: Input[str]
    """
    The name of the scope that the selector applies to.
    """
    values: NotRequired[Input[Sequence[Input[str]]]]
    """
    An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.
    """

class SeccompProfilePatchArgsDict(TypedDict):
    """
    SeccompProfile defines a pod/container's seccomp profile settings. Only one profile source may be set.
    """
    localhost_profile: NotRequired[Input[str]]
    """
    localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.
    """
    type: NotRequired[Input[str]]
    """
    type indicates which kind of seccomp profile will be applied. Valid options are:

    Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.
    """

class SeccompProfileArgsDict(TypedDict):
    """
    SeccompProfile defines a pod/container's seccomp profile settings. Only one profile source may be set.
    """
    type: Input[str]
    """
    type indicates which kind of seccomp profile will be applied. Valid options are:

    Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.
    """
    localhost_profile: NotRequired[Input[str]]
    """
    localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.
    """

class SecretEnvSourcePatchArgsDict(TypedDict):
    """
    SecretEnvSource selects a Secret to populate the environment variables with.

    The contents of the target Secret's Data field will represent the key-value pairs as environment variables.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    Specify whether the Secret must be defined
    """

class SecretEnvSourceArgsDict(TypedDict):
    """
    SecretEnvSource selects a Secret to populate the environment variables with.

    The contents of the target Secret's Data field will represent the key-value pairs as environment variables.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    Specify whether the Secret must be defined
    """

class SecretKeySelectorPatchArgsDict(TypedDict):
    """
    SecretKeySelector selects a key of a Secret.
    """
    key: NotRequired[Input[str]]
    """
    The key of the secret to select from.  Must be a valid secret key.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    Specify whether the Secret or its key must be defined
    """

class SecretKeySelectorArgsDict(TypedDict):
    """
    SecretKeySelector selects a key of a Secret.
    """
    key: Input[str]
    """
    The key of the secret to select from.  Must be a valid secret key.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    Specify whether the Secret or its key must be defined
    """

class SecretProjectionPatchArgsDict(TypedDict):
    """
    Adapts a secret into a projected volume.

    The contents of the target Secret's Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode.
    """
    items: NotRequired[Input[Sequence[Input['KeyToPathPatchArgsDict']]]]
    """
    items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    optional field specify whether the Secret or its key must be defined
    """

class SecretProjectionArgsDict(TypedDict):
    """
    Adapts a secret into a projected volume.

    The contents of the target Secret's Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode.
    """
    items: NotRequired[Input[Sequence[Input['KeyToPathArgsDict']]]]
    """
    items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    """
    name: NotRequired[Input[str]]
    """
    Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    optional: NotRequired[Input[bool]]
    """
    optional field specify whether the Secret or its key must be defined
    """

class SecretReferencePatchArgsDict(TypedDict):
    """
    SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace
    """
    name: NotRequired[Input[str]]
    """
    name is unique within a namespace to reference a secret resource.
    """
    namespace: NotRequired[Input[str]]
    """
    namespace defines the space within which the secret name must be unique.
    """

class SecretReferenceArgsDict(TypedDict):
    """
    SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace
    """
    name: NotRequired[Input[str]]
    """
    name is unique within a namespace to reference a secret resource.
    """
    namespace: NotRequired[Input[str]]
    """
    namespace defines the space within which the secret name must be unique.
    """

class SecretVolumeSourcePatchArgsDict(TypedDict):
    """
    Adapts a Secret into a volume.

    The contents of the target Secret's Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.
    """
    default_mode: NotRequired[Input[int]]
    """
    defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    items: NotRequired[Input[Sequence[Input['KeyToPathPatchArgsDict']]]]
    """
    items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    """
    optional: NotRequired[Input[bool]]
    """
    optional field specify whether the Secret or its keys must be defined
    """
    secret_name: NotRequired[Input[str]]
    """
    secretName is the name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    """

class SecretVolumeSourceArgsDict(TypedDict):
    """
    Adapts a Secret into a volume.

    The contents of the target Secret's Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.
    """
    default_mode: NotRequired[Input[int]]
    """
    defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
    """
    items: NotRequired[Input[Sequence[Input['KeyToPathArgsDict']]]]
    """
    items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
    """
    optional: NotRequired[Input[bool]]
    """
    optional field specify whether the Secret or its keys must be defined
    """
    secret_name: NotRequired[Input[str]]
    """
    secretName is the name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    """

class SecretArgsDict(TypedDict):
    """
    Secret holds secret data of a certain type. The total bytes of the values in the Data field must be less than MaxSecretSize bytes.

    Note: While Pulumi automatically encrypts the 'data' and 'stringData'
    fields, this encryption only applies to Pulumi's context, including the state file, 
    the Service, the CLI, etc. Kubernetes does not encrypt Secret resources by default,
    and the contents are visible to users with access to the Secret in Kubernetes using
    tools like 'kubectl'.

    For more information on securing Kubernetes Secrets, see the following links:
    https://kubernetes.io/docs/concepts/configuration/secret/#security-properties
    https://kubernetes.io/docs/concepts/configuration/secret/#risks
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    data: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4
    """
    immutable: NotRequired[Input[bool]]
    """
    Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil.
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    string_data: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API.
    """
    type: NotRequired[Input[str]]
    """
    Used to facilitate programmatic handling of secret data. More info: https://kubernetes.io/docs/concepts/configuration/secret/#secret-types
    """

class SecurityContextPatchArgsDict(TypedDict):
    """
    SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext.  When both are set, the values in SecurityContext take precedence.
    """
    allow_privilege_escalation: NotRequired[Input[bool]]
    """
    AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.
    """
    app_armor_profile: NotRequired[Input['AppArmorProfilePatchArgsDict']]
    """
    appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod's appArmorProfile. Note that this field cannot be set when spec.os.name is windows.
    """
    capabilities: NotRequired[Input['CapabilitiesPatchArgsDict']]
    """
    The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.
    """
    privileged: NotRequired[Input[bool]]
    """
    Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.
    """
    proc_mount: NotRequired[Input[str]]
    """
    procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.
    """
    read_only_root_filesystem: NotRequired[Input[bool]]
    """
    Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.
    """
    run_as_group: NotRequired[Input[int]]
    """
    The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.
    """
    run_as_non_root: NotRequired[Input[bool]]
    """
    Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    run_as_user: NotRequired[Input[int]]
    """
    The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.
    """
    se_linux_options: NotRequired[Input['SELinuxOptionsPatchArgsDict']]
    """
    The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.
    """
    seccomp_profile: NotRequired[Input['SeccompProfilePatchArgsDict']]
    """
    The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.
    """
    windows_options: NotRequired[Input['WindowsSecurityContextOptionsPatchArgsDict']]
    """
    The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.
    """

class SecurityContextArgsDict(TypedDict):
    """
    SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext.  When both are set, the values in SecurityContext take precedence.
    """
    allow_privilege_escalation: NotRequired[Input[bool]]
    """
    AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.
    """
    app_armor_profile: NotRequired[Input['AppArmorProfileArgsDict']]
    """
    appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod's appArmorProfile. Note that this field cannot be set when spec.os.name is windows.
    """
    capabilities: NotRequired[Input['CapabilitiesArgsDict']]
    """
    The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.
    """
    privileged: NotRequired[Input[bool]]
    """
    Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.
    """
    proc_mount: NotRequired[Input[str]]
    """
    procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.
    """
    read_only_root_filesystem: NotRequired[Input[bool]]
    """
    Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.
    """
    run_as_group: NotRequired[Input[int]]
    """
    The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.
    """
    run_as_non_root: NotRequired[Input[bool]]
    """
    Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """
    run_as_user: NotRequired[Input[int]]
    """
    The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.
    """
    se_linux_options: NotRequired[Input['SELinuxOptionsArgsDict']]
    """
    The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.
    """
    seccomp_profile: NotRequired[Input['SeccompProfileArgsDict']]
    """
    The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.
    """
    windows_options: NotRequired[Input['WindowsSecurityContextOptionsArgsDict']]
    """
    The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.
    """

class ServiceAccountTokenProjectionPatchArgsDict(TypedDict):
    """
    ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise).
    """
    audience: NotRequired[Input[str]]
    """
    audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.
    """
    expiration_seconds: NotRequired[Input[int]]
    """
    expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.
    """
    path: NotRequired[Input[str]]
    """
    path is the path relative to the mount point of the file to project the token into.
    """

class ServiceAccountTokenProjectionArgsDict(TypedDict):
    """
    ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise).
    """
    path: Input[str]
    """
    path is the path relative to the mount point of the file to project the token into.
    """
    audience: NotRequired[Input[str]]
    """
    audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.
    """
    expiration_seconds: NotRequired[Input[int]]
    """
    expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.
    """

class ServiceAccountArgsDict(TypedDict):
    """
    ServiceAccount binds together: * a name, understood by users, and perhaps by peripheral systems, for an identity * a principal that can be authenticated and authorized * a set of secrets
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    automount_service_account_token: NotRequired[Input[bool]]
    """
    AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level.
    """
    image_pull_secrets: NotRequired[Input[Sequence[Input['LocalObjectReferenceArgsDict']]]]
    """
    ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    secrets: NotRequired[Input[Sequence[Input['ObjectReferenceArgsDict']]]]
    """
    Secrets is a list of the secrets in the same namespace that pods running using this ServiceAccount are allowed to use. Pods are only limited to this list if this service account has a "kubernetes.io/enforce-mountable-secrets" annotation set to "true". This field should not be used to find auto-generated service account token secrets for use outside of pods. Instead, tokens can be requested directly using the TokenRequest API, or service account token secrets can be manually created. More info: https://kubernetes.io/docs/concepts/configuration/secret
    """

class ServicePortPatchArgsDict(TypedDict):
    """
    ServicePort contains information on service's port.
    """
    app_protocol: NotRequired[Input[str]]
    """
    The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:

    * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).

    * Kubernetes-defined prefixed names:
      * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
      * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
      * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455

    * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.
    """
    name: NotRequired[Input[str]]
    """
    The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service.
    """
    node_port: NotRequired[Input[int]]
    """
    The port on each node on which this service is exposed when type is NodePort or LoadBalancer.  Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail.  If not specified, a port will be allocated if this Service requires one.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type from NodePort to ClusterIP). More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
    """
    port: NotRequired[Input[int]]
    """
    The port that will be exposed by this service.
    """
    protocol: NotRequired[Input[str]]
    """
    The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP.
    """
    target_port: NotRequired[Input[Union[int, str]]]
    """
    Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service
    """

class ServicePortArgsDict(TypedDict):
    """
    ServicePort contains information on service's port.
    """
    port: Input[int]
    """
    The port that will be exposed by this service.
    """
    app_protocol: NotRequired[Input[str]]
    """
    The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:

    * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).

    * Kubernetes-defined prefixed names:
      * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
      * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
      * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455

    * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.
    """
    name: NotRequired[Input[str]]
    """
    The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service.
    """
    node_port: NotRequired[Input[int]]
    """
    The port on each node on which this service is exposed when type is NodePort or LoadBalancer.  Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail.  If not specified, a port will be allocated if this Service requires one.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type from NodePort to ClusterIP). More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
    """
    protocol: NotRequired[Input[str]]
    """
    The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP.
    """
    target_port: NotRequired[Input[Union[int, str]]]
    """
    Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service
    """

class ServiceSpecPatchArgsDict(TypedDict):
    """
    ServiceSpec describes the attributes that a user creates on a service.
    """
    allocate_load_balancer_node_ports: NotRequired[Input[bool]]
    """
    allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer.  Default is "true". It may be set to "false" if the cluster load-balancer does not rely on NodePorts.  If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type.
    """
    cluster_ip: NotRequired[Input[str]]
    """
    clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address. Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    """
    cluster_ips: NotRequired[Input[Sequence[Input[str]]]]
    """
    ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly.  If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address.  Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName.  If this field is not specified, it will be initialized from the clusterIP field.  If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.

    This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    """
    external_ips: NotRequired[Input[Sequence[Input[str]]]]
    """
    externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.
    """
    external_name: NotRequired[Input[str]]
    """
    externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved.  Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires `type` to be "ExternalName".
    """
    external_traffic_policy: NotRequired[Input[str]]
    """
    externalTrafficPolicy describes how nodes distribute service traffic they receive on one of the Service's "externally-facing" addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If set to "Local", the proxy will configure the service in a way that assumes that external load balancers will take care of balancing the service traffic between nodes, and so each node will deliver traffic only to the node-local endpoints of the service, without masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be dropped.) The default value, "Cluster", uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). Note that traffic sent to an External IP or LoadBalancer IP from within the cluster will always get "Cluster" semantics, but clients sending to a NodePort from within the cluster may need to take traffic policy into account when picking a node.
    """
    health_check_node_port: NotRequired[Input[int]]
    """
    healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used.  If not specified, a value will be automatically allocated.  External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type). This field cannot be updated once set.
    """
    internal_traffic_policy: NotRequired[Input[str]]
    """
    InternalTrafficPolicy describes how nodes distribute service traffic they receive on the ClusterIP. If set to "Local", the proxy will assume that pods only want to talk to endpoints of the service on the same node as the pod, dropping the traffic if there are no local endpoints. The default value, "Cluster", uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features).
    """
    ip_families: NotRequired[Input[Sequence[Input[str]]]]
    """
    IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service. Valid values are "IPv4" and "IPv6".  This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to "headless" services. This field will be wiped when updating a Service to type ExternalName.

    This field may hold a maximum of two entries (dual-stack families, in either order).  These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field.
    """
    ip_family: NotRequired[Input[str]]
    """
    ipFamily specifies whether this Service has a preference for a particular IP family (e.g. IPv4 vs. IPv6).  If a specific IP family is requested, the clusterIP field will be allocated from that family, if it is available in the cluster.  If no IP family is requested, the cluster's primary IP family will be used. Other IP fields (loadBalancerIP, loadBalancerSourceRanges, externalIPs) and controllers which allocate external load-balancers should use the same IP family.  Endpoints for this Service will be of this family.  This field is immutable after creation. Assigning a ServiceIPFamily not available in the cluster (e.g. IPv6 in IPv4 only cluster) is an error condition and will fail during clusterIP assignment.
    """
    ip_family_policy: NotRequired[Input[str]]
    """
    IPFamilyPolicy represents the dual-stack-ness requested or required by this Service. If there is no value provided, then this field will be set to SingleStack. Services can be "SingleStack" (a single IP family), "PreferDualStack" (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or "RequireDualStack" (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. This field will be wiped when updating a service to type ExternalName.
    """
    load_balancer_class: NotRequired[Input[str]]
    """
    loadBalancerClass is the class of the load balancer implementation this Service belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. "internal-vip" or "example.com/internal-vip". Unprefixed names are reserved for end-users. This field can only be set when the Service type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a Service to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type.
    """
    load_balancer_ip: NotRequired[Input[str]]
    """
    Only applies to Service Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations. Using it is non-portable and it may not support dual-stack. Users are encouraged to use implementation-specific annotations when available.
    """
    load_balancer_source_ranges: NotRequired[Input[Sequence[Input[str]]]]
    """
    If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature." More info: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
    """
    ports: NotRequired[Input[Sequence[Input['ServicePortPatchArgsDict']]]]
    """
    The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    """
    publish_not_ready_addresses: NotRequired[Input[bool]]
    """
    publishNotReadyAddresses indicates that any agent which deals with endpoints for this Service should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless Service to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered "ready" even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior.
    """
    selector: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/
    """
    session_affinity: NotRequired[Input[str]]
    """
    Supports "ClientIP" and "None". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    """
    session_affinity_config: NotRequired[Input['SessionAffinityConfigPatchArgsDict']]
    """
    sessionAffinityConfig contains the configurations of session affinity.
    """
    topology_keys: NotRequired[Input[Sequence[Input[str]]]]
    """
    topologyKeys is a preference-order list of topology keys which implementations of services should use to preferentially sort endpoints when accessing this Service, it can not be used at the same time as externalTrafficPolicy=Local. Topology keys must be valid label keys and at most 16 keys may be specified. Endpoints are chosen based on the first topology key with available backends. If this field is specified and all entries have no backends that match the topology of the client, the service has no backends for that client and connections should fail. The special value "*" may be used to mean "any topology". This catch-all value, if used, only makes sense as the last value in the list. If this is not specified or empty, no topology constraints will be applied.
    """
    traffic_distribution: NotRequired[Input[str]]
    """
    TrafficDistribution offers a way to express preferences for how traffic is distributed to Service endpoints. Implementations can use this field as a hint, but are not required to guarantee strict adherence. If the field is not set, the implementation will apply its default routing strategy. If set to "PreferClose", implementations should prioritize endpoints that are topologically close (e.g., same zone).
    """
    type: NotRequired[Input[Union[str, 'ServiceSpecType']]]
    """
    type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. "ClusterIP" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is "None", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. "NodePort" builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. "LoadBalancer" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. "ExternalName" aliases this service to the specified externalName. Several other fields do not apply to ExternalName services. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types
    """

class ServiceSpecArgsDict(TypedDict):
    """
    ServiceSpec describes the attributes that a user creates on a service.
    """
    allocate_load_balancer_node_ports: NotRequired[Input[bool]]
    """
    allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer.  Default is "true". It may be set to "false" if the cluster load-balancer does not rely on NodePorts.  If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type.
    """
    cluster_ip: NotRequired[Input[str]]
    """
    clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address. Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    """
    cluster_ips: NotRequired[Input[Sequence[Input[str]]]]
    """
    ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly.  If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address.  Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName.  If this field is not specified, it will be initialized from the clusterIP field.  If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.

    This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    """
    external_ips: NotRequired[Input[Sequence[Input[str]]]]
    """
    externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.
    """
    external_name: NotRequired[Input[str]]
    """
    externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved.  Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires `type` to be "ExternalName".
    """
    external_traffic_policy: NotRequired[Input[str]]
    """
    externalTrafficPolicy describes how nodes distribute service traffic they receive on one of the Service's "externally-facing" addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If set to "Local", the proxy will configure the service in a way that assumes that external load balancers will take care of balancing the service traffic between nodes, and so each node will deliver traffic only to the node-local endpoints of the service, without masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be dropped.) The default value, "Cluster", uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). Note that traffic sent to an External IP or LoadBalancer IP from within the cluster will always get "Cluster" semantics, but clients sending to a NodePort from within the cluster may need to take traffic policy into account when picking a node.
    """
    health_check_node_port: NotRequired[Input[int]]
    """
    healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used.  If not specified, a value will be automatically allocated.  External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type). This field cannot be updated once set.
    """
    internal_traffic_policy: NotRequired[Input[str]]
    """
    InternalTrafficPolicy describes how nodes distribute service traffic they receive on the ClusterIP. If set to "Local", the proxy will assume that pods only want to talk to endpoints of the service on the same node as the pod, dropping the traffic if there are no local endpoints. The default value, "Cluster", uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features).
    """
    ip_families: NotRequired[Input[Sequence[Input[str]]]]
    """
    IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service. Valid values are "IPv4" and "IPv6".  This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to "headless" services. This field will be wiped when updating a Service to type ExternalName.

    This field may hold a maximum of two entries (dual-stack families, in either order).  These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field.
    """
    ip_family: NotRequired[Input[str]]
    """
    ipFamily specifies whether this Service has a preference for a particular IP family (e.g. IPv4 vs. IPv6).  If a specific IP family is requested, the clusterIP field will be allocated from that family, if it is available in the cluster.  If no IP family is requested, the cluster's primary IP family will be used. Other IP fields (loadBalancerIP, loadBalancerSourceRanges, externalIPs) and controllers which allocate external load-balancers should use the same IP family.  Endpoints for this Service will be of this family.  This field is immutable after creation. Assigning a ServiceIPFamily not available in the cluster (e.g. IPv6 in IPv4 only cluster) is an error condition and will fail during clusterIP assignment.
    """
    ip_family_policy: NotRequired[Input[str]]
    """
    IPFamilyPolicy represents the dual-stack-ness requested or required by this Service. If there is no value provided, then this field will be set to SingleStack. Services can be "SingleStack" (a single IP family), "PreferDualStack" (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or "RequireDualStack" (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. This field will be wiped when updating a service to type ExternalName.
    """
    load_balancer_class: NotRequired[Input[str]]
    """
    loadBalancerClass is the class of the load balancer implementation this Service belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. "internal-vip" or "example.com/internal-vip". Unprefixed names are reserved for end-users. This field can only be set when the Service type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a Service to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type.
    """
    load_balancer_ip: NotRequired[Input[str]]
    """
    Only applies to Service Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations. Using it is non-portable and it may not support dual-stack. Users are encouraged to use implementation-specific annotations when available.
    """
    load_balancer_source_ranges: NotRequired[Input[Sequence[Input[str]]]]
    """
    If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature." More info: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
    """
    ports: NotRequired[Input[Sequence[Input['ServicePortArgsDict']]]]
    """
    The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    """
    publish_not_ready_addresses: NotRequired[Input[bool]]
    """
    publishNotReadyAddresses indicates that any agent which deals with endpoints for this Service should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless Service to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered "ready" even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior.
    """
    selector: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/
    """
    session_affinity: NotRequired[Input[str]]
    """
    Supports "ClientIP" and "None". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
    """
    session_affinity_config: NotRequired[Input['SessionAffinityConfigArgsDict']]
    """
    sessionAffinityConfig contains the configurations of session affinity.
    """
    topology_keys: NotRequired[Input[Sequence[Input[str]]]]
    """
    topologyKeys is a preference-order list of topology keys which implementations of services should use to preferentially sort endpoints when accessing this Service, it can not be used at the same time as externalTrafficPolicy=Local. Topology keys must be valid label keys and at most 16 keys may be specified. Endpoints are chosen based on the first topology key with available backends. If this field is specified and all entries have no backends that match the topology of the client, the service has no backends for that client and connections should fail. The special value "*" may be used to mean "any topology". This catch-all value, if used, only makes sense as the last value in the list. If this is not specified or empty, no topology constraints will be applied.
    """
    traffic_distribution: NotRequired[Input[str]]
    """
    TrafficDistribution offers a way to express preferences for how traffic is distributed to Service endpoints. Implementations can use this field as a hint, but are not required to guarantee strict adherence. If the field is not set, the implementation will apply its default routing strategy. If set to "PreferClose", implementations should prioritize endpoints that are topologically close (e.g., same zone).
    """
    type: NotRequired[Input[Union[str, 'ServiceSpecType']]]
    """
    type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. "ClusterIP" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is "None", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. "NodePort" builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. "LoadBalancer" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. "ExternalName" aliases this service to the specified externalName. Several other fields do not apply to ExternalName services. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types
    """

class ServiceStatusArgsDict(TypedDict):
    """
    ServiceStatus represents the current status of a service.
    """
    conditions: NotRequired[Input[Sequence[Input['ConditionArgsDict']]]]
    """
    Current service state
    """
    load_balancer: NotRequired[Input['LoadBalancerStatusArgsDict']]
    """
    LoadBalancer contains the current status of the load-balancer, if one is present.
    """

class ServiceArgsDict(TypedDict):
    """
    Service is a named abstraction of software service (for example, mysql) consisting of local port (for example 3306) that the proxy listens on, and the selector that determines which pods will answer requests sent through the proxy.

    This resource waits until its status is ready before registering success
    for create/update, and populating output properties from the current state of the resource.
    The following conditions are used to determine whether the resource creation has
    succeeded or failed:

    1. Service object exists.
    2. Related Endpoint objects are created. Each time we get an update, wait 10 seconds
       for any stragglers.
    3. The endpoints objects target some number of living objects (unless the Service is
       an "empty headless" Service [1] or a Service with '.spec.type: ExternalName').
    4. External IP address is allocated (if Service has '.spec.type: LoadBalancer').

    Known limitations: 
    Services targeting ReplicaSets (and, by extension, Deployments,
    StatefulSets, etc.) with '.spec.replicas' set to 0 are not handled, and will time
    out. To work around this limitation, set 'pulumi.com/skipAwait: "true"' on
    '.metadata.annotations' for the Service. Work to handle this case is in progress [2].

    [1] https://kubernetes.io/docs/concepts/services-networking/service/#headless-services
    [2] https://github.com/pulumi/pulumi-kubernetes/pull/703

    If the Service has not reached a Ready state after 10 minutes, it will
    time out and mark the resource update as Failed. You can override the default timeout value
    by setting the 'customTimeouts' option on the resource.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['ServiceSpecArgsDict']]
    """
    Spec defines the behavior of a service. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    status: NotRequired[Input['ServiceStatusArgsDict']]
    """
    Most recently observed status of the service. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class SessionAffinityConfigPatchArgsDict(TypedDict):
    """
    SessionAffinityConfig represents the configurations of session affinity.
    """
    client_ip: NotRequired[Input['ClientIPConfigPatchArgsDict']]
    """
    clientIP contains the configurations of Client IP based session affinity.
    """

class SessionAffinityConfigArgsDict(TypedDict):
    """
    SessionAffinityConfig represents the configurations of session affinity.
    """
    client_ip: NotRequired[Input['ClientIPConfigArgsDict']]
    """
    clientIP contains the configurations of Client IP based session affinity.
    """

class SleepActionPatchArgsDict(TypedDict):
    """
    SleepAction describes a "sleep" action.
    """
    seconds: NotRequired[Input[int]]
    """
    Seconds is the number of seconds to sleep.
    """

class SleepActionArgsDict(TypedDict):
    """
    SleepAction describes a "sleep" action.
    """
    seconds: Input[int]
    """
    Seconds is the number of seconds to sleep.
    """

class StorageOSPersistentVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a StorageOS persistent volume resource.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['ObjectReferencePatchArgsDict']]
    """
    secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.
    """
    volume_namespace: NotRequired[Input[str]]
    """
    volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.
    """

class StorageOSPersistentVolumeSourceArgsDict(TypedDict):
    """
    Represents a StorageOS persistent volume resource.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['ObjectReferenceArgsDict']]
    """
    secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.
    """
    volume_namespace: NotRequired[Input[str]]
    """
    volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.
    """

class StorageOSVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a StorageOS persistent volume resource.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['LocalObjectReferencePatchArgsDict']]
    """
    secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.
    """
    volume_namespace: NotRequired[Input[str]]
    """
    volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.
    """

class StorageOSVolumeSourceArgsDict(TypedDict):
    """
    Represents a StorageOS persistent volume resource.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    read_only: NotRequired[Input[bool]]
    """
    readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.
    """
    secret_ref: NotRequired[Input['LocalObjectReferenceArgsDict']]
    """
    secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.
    """
    volume_name: NotRequired[Input[str]]
    """
    volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.
    """
    volume_namespace: NotRequired[Input[str]]
    """
    volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.
    """

class SysctlPatchArgsDict(TypedDict):
    """
    Sysctl defines a kernel parameter to be set
    """
    name: NotRequired[Input[str]]
    """
    Name of a property to set
    """
    value: NotRequired[Input[str]]
    """
    Value of a property to set
    """

class SysctlArgsDict(TypedDict):
    """
    Sysctl defines a kernel parameter to be set
    """
    name: Input[str]
    """
    Name of a property to set
    """
    value: Input[str]
    """
    Value of a property to set
    """

class TCPSocketActionPatchArgsDict(TypedDict):
    """
    TCPSocketAction describes an action based on opening a socket
    """
    host: NotRequired[Input[str]]
    """
    Optional: Host name to connect to, defaults to the pod IP.
    """
    port: NotRequired[Input[Union[int, str]]]
    """
    Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    """

class TCPSocketActionArgsDict(TypedDict):
    """
    TCPSocketAction describes an action based on opening a socket
    """
    port: Input[Union[int, str]]
    """
    Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.
    """
    host: NotRequired[Input[str]]
    """
    Optional: Host name to connect to, defaults to the pod IP.
    """

class TaintPatchArgsDict(TypedDict):
    """
    The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint.
    """
    effect: NotRequired[Input[str]]
    """
    Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.
    """
    key: NotRequired[Input[str]]
    """
    Required. The taint key to be applied to a node.
    """
    time_added: NotRequired[Input[str]]
    """
    TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.
    """
    value: NotRequired[Input[str]]
    """
    The taint value corresponding to the taint key.
    """

class TaintArgsDict(TypedDict):
    """
    The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint.
    """
    effect: Input[str]
    """
    Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.
    """
    key: Input[str]
    """
    Required. The taint key to be applied to a node.
    """
    time_added: NotRequired[Input[str]]
    """
    TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.
    """
    value: NotRequired[Input[str]]
    """
    The taint value corresponding to the taint key.
    """

class TolerationPatchArgsDict(TypedDict):
    """
    The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.
    """
    effect: NotRequired[Input[str]]
    """
    Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.
    """
    key: NotRequired[Input[str]]
    """
    Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.
    """
    operator: NotRequired[Input[str]]
    """
    Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.
    """
    toleration_seconds: NotRequired[Input[int]]
    """
    TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.
    """
    value: NotRequired[Input[str]]
    """
    Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.
    """

class TolerationArgsDict(TypedDict):
    """
    The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.
    """
    effect: NotRequired[Input[str]]
    """
    Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.
    """
    key: NotRequired[Input[str]]
    """
    Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.
    """
    operator: NotRequired[Input[str]]
    """
    Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.
    """
    toleration_seconds: NotRequired[Input[int]]
    """
    TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.
    """
    value: NotRequired[Input[str]]
    """
    Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.
    """

class TopologySelectorLabelRequirementPatchArgsDict(TypedDict):
    """
    A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future.
    """
    key: NotRequired[Input[str]]
    """
    The label key that the selector applies to.
    """
    values: NotRequired[Input[Sequence[Input[str]]]]
    """
    An array of string values. One value must match the label to be selected. Each entry in Values is ORed.
    """

class TopologySelectorLabelRequirementArgsDict(TypedDict):
    """
    A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future.
    """
    key: Input[str]
    """
    The label key that the selector applies to.
    """
    values: Input[Sequence[Input[str]]]
    """
    An array of string values. One value must match the label to be selected. Each entry in Values is ORed.
    """

class TopologySelectorTermPatchArgsDict(TypedDict):
    """
    A topology selector term represents the result of label queries. A null or empty topology selector term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as NodeSelectorTerm. This is an alpha feature and may change in the future.
    """
    match_label_expressions: NotRequired[Input[Sequence[Input['TopologySelectorLabelRequirementPatchArgsDict']]]]
    """
    A list of topology selector requirements by labels.
    """

class TopologySelectorTermArgsDict(TypedDict):
    """
    A topology selector term represents the result of label queries. A null or empty topology selector term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as NodeSelectorTerm. This is an alpha feature and may change in the future.
    """
    match_label_expressions: NotRequired[Input[Sequence[Input['TopologySelectorLabelRequirementArgsDict']]]]
    """
    A list of topology selector requirements by labels.
    """

class TopologySpreadConstraintPatchArgsDict(TypedDict):
    """
    TopologySpreadConstraint specifies how to spread matching pods among the given topology.
    """
    label_selector: NotRequired[Input['LabelSelectorPatchArgsDict']]
    """
    LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.
    """
    match_label_keys: NotRequired[Input[Sequence[Input[str]]]]
    """
    MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn't set. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.

    This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).
    """
    max_skew: NotRequired[Input[int]]
    """
    MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.
    """
    min_domains: NotRequired[Input[int]]
    """
    MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats "global minimum" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.

    For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so "global minimum" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.
    """
    node_affinity_policy: NotRequired[Input[str]]
    """
    NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.

    If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.
    """
    node_taints_policy: NotRequired[Input[str]]
    """
    NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.

    If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.
    """
    topology_key: NotRequired[Input[str]]
    """
    TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is "kubernetes.io/hostname", each Node is a domain of that topology. And, if TopologyKey is "topology.kubernetes.io/zone", each zone is a domain of that topology. It's a required field.
    """
    when_unsatisfiable: NotRequired[Input[str]]
    """
    WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,
      but giving higher precedence to topologies that would help reduce the
      skew.
    A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assignment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.
    """

class TopologySpreadConstraintArgsDict(TypedDict):
    """
    TopologySpreadConstraint specifies how to spread matching pods among the given topology.
    """
    max_skew: Input[int]
    """
    MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.
    """
    topology_key: Input[str]
    """
    TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is "kubernetes.io/hostname", each Node is a domain of that topology. And, if TopologyKey is "topology.kubernetes.io/zone", each zone is a domain of that topology. It's a required field.
    """
    when_unsatisfiable: Input[str]
    """
    WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,
      but giving higher precedence to topologies that would help reduce the
      skew.
    A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assignment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.
    """
    label_selector: NotRequired[Input['LabelSelectorArgsDict']]
    """
    LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.
    """
    match_label_keys: NotRequired[Input[Sequence[Input[str]]]]
    """
    MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn't set. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.

    This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).
    """
    min_domains: NotRequired[Input[int]]
    """
    MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats "global minimum" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.

    For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so "global minimum" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.
    """
    node_affinity_policy: NotRequired[Input[str]]
    """
    NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.

    If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.
    """
    node_taints_policy: NotRequired[Input[str]]
    """
    NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.

    If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.
    """

class TypedLocalObjectReferencePatchArgsDict(TypedDict):
    """
    TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.
    """
    api_group: NotRequired[Input[str]]
    """
    APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.
    """
    kind: NotRequired[Input[str]]
    """
    Kind is the type of resource being referenced
    """
    name: NotRequired[Input[str]]
    """
    Name is the name of resource being referenced
    """

class TypedLocalObjectReferenceArgsDict(TypedDict):
    """
    TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.
    """
    kind: Input[str]
    """
    Kind is the type of resource being referenced
    """
    name: Input[str]
    """
    Name is the name of resource being referenced
    """
    api_group: NotRequired[Input[str]]
    """
    APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.
    """

class TypedObjectReferencePatchArgsDict(TypedDict):
    api_group: NotRequired[Input[str]]
    """
    APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.
    """
    kind: NotRequired[Input[str]]
    """
    Kind is the type of resource being referenced
    """
    name: NotRequired[Input[str]]
    """
    Name is the name of resource being referenced
    """
    namespace: NotRequired[Input[str]]
    """
    Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled.
    """

class TypedObjectReferenceArgsDict(TypedDict):
    kind: Input[str]
    """
    Kind is the type of resource being referenced
    """
    name: Input[str]
    """
    Name is the name of resource being referenced
    """
    api_group: NotRequired[Input[str]]
    """
    APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.
    """
    namespace: NotRequired[Input[str]]
    """
    Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled.
    """

class VolumeDevicePatchArgsDict(TypedDict):
    """
    volumeDevice describes a mapping of a raw block device within a container.
    """
    device_path: NotRequired[Input[str]]
    """
    devicePath is the path inside of the container that the device will be mapped to.
    """
    name: NotRequired[Input[str]]
    """
    name must match the name of a persistentVolumeClaim in the pod
    """

class VolumeDeviceArgsDict(TypedDict):
    """
    volumeDevice describes a mapping of a raw block device within a container.
    """
    device_path: Input[str]
    """
    devicePath is the path inside of the container that the device will be mapped to.
    """
    name: Input[str]
    """
    name must match the name of a persistentVolumeClaim in the pod
    """

class VolumeMountPatchArgsDict(TypedDict):
    """
    VolumeMount describes a mounting of a Volume within a container.
    """
    mount_path: NotRequired[Input[str]]
    """
    Path within the container at which the volume should be mounted.  Must not contain ':'.
    """
    mount_propagation: NotRequired[Input[str]]
    """
    mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).
    """
    name: NotRequired[Input[str]]
    """
    This must match the Name of a Volume.
    """
    read_only: NotRequired[Input[bool]]
    """
    Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.
    """
    recursive_read_only: NotRequired[Input[str]]
    """
    RecursiveReadOnly specifies whether read-only mounts should be handled recursively.

    If ReadOnly is false, this field has no meaning and must be unspecified.

    If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only.  If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime.  If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.

    If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).

    If this field is not specified, it is treated as an equivalent of Disabled.
    """
    sub_path: NotRequired[Input[str]]
    """
    Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).
    """
    sub_path_expr: NotRequired[Input[str]]
    """
    Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.
    """

class VolumeMountStatusArgsDict(TypedDict):
    """
    VolumeMountStatus shows status of volume mounts.
    """
    mount_path: Input[str]
    """
    MountPath corresponds to the original VolumeMount.
    """
    name: Input[str]
    """
    Name corresponds to the name of the original VolumeMount.
    """
    read_only: NotRequired[Input[bool]]
    """
    ReadOnly corresponds to the original VolumeMount.
    """
    recursive_read_only: NotRequired[Input[str]]
    """
    RecursiveReadOnly must be set to Disabled, Enabled, or unspecified (for non-readonly mounts). An IfPossible value in the original VolumeMount must be translated to Disabled or Enabled, depending on the mount result.
    """

class VolumeMountArgsDict(TypedDict):
    """
    VolumeMount describes a mounting of a Volume within a container.
    """
    mount_path: Input[str]
    """
    Path within the container at which the volume should be mounted.  Must not contain ':'.
    """
    name: Input[str]
    """
    This must match the Name of a Volume.
    """
    mount_propagation: NotRequired[Input[str]]
    """
    mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).
    """
    read_only: NotRequired[Input[bool]]
    """
    Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.
    """
    recursive_read_only: NotRequired[Input[str]]
    """
    RecursiveReadOnly specifies whether read-only mounts should be handled recursively.

    If ReadOnly is false, this field has no meaning and must be unspecified.

    If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only.  If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime.  If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.

    If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).

    If this field is not specified, it is treated as an equivalent of Disabled.
    """
    sub_path: NotRequired[Input[str]]
    """
    Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).
    """
    sub_path_expr: NotRequired[Input[str]]
    """
    Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.
    """

class VolumeNodeAffinityPatchArgsDict(TypedDict):
    """
    VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from.
    """
    required: NotRequired[Input['NodeSelectorPatchArgsDict']]
    """
    required specifies hard node constraints that must be met.
    """

class VolumeNodeAffinityArgsDict(TypedDict):
    """
    VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from.
    """
    required: NotRequired[Input['NodeSelectorArgsDict']]
    """
    required specifies hard node constraints that must be met.
    """

class VolumePatchArgsDict(TypedDict):
    """
    Volume represents a named volume in a pod that may be accessed by any container in the pod.
    """
    aws_elastic_block_store: NotRequired[Input['AWSElasticBlockStoreVolumeSourcePatchArgsDict']]
    """
    awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    azure_disk: NotRequired[Input['AzureDiskVolumeSourcePatchArgsDict']]
    """
    azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    """
    azure_file: NotRequired[Input['AzureFileVolumeSourcePatchArgsDict']]
    """
    azureFile represents an Azure File Service mount on the host and bind mount to the pod.
    """
    cephfs: NotRequired[Input['CephFSVolumeSourcePatchArgsDict']]
    """
    cephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    """
    cinder: NotRequired[Input['CinderVolumeSourcePatchArgsDict']]
    """
    cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    config_map: NotRequired[Input['ConfigMapVolumeSourcePatchArgsDict']]
    """
    configMap represents a configMap that should populate this volume
    """
    csi: NotRequired[Input['CSIVolumeSourcePatchArgsDict']]
    """
    csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers (Beta feature).
    """
    downward_api: NotRequired[Input['DownwardAPIVolumeSourcePatchArgsDict']]
    """
    downwardAPI represents downward API about the pod that should populate this volume
    """
    empty_dir: NotRequired[Input['EmptyDirVolumeSourcePatchArgsDict']]
    """
    emptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    """
    ephemeral: NotRequired[Input['EphemeralVolumeSourcePatchArgsDict']]
    """
    ephemeral represents a volume that is handled by a cluster storage driver. The volume's lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.

    Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity
       tracking are needed,
    c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through
       a PersistentVolumeClaim (see EphemeralVolumeSource for more
       information on the connection between this volume type
       and PersistentVolumeClaim).

    Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.

    Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.

    A pod can use both types of ephemeral volumes and persistent volumes at the same time.
    """
    fc: NotRequired[Input['FCVolumeSourcePatchArgsDict']]
    """
    fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    """
    flex_volume: NotRequired[Input['FlexVolumeSourcePatchArgsDict']]
    """
    flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    """
    flocker: NotRequired[Input['FlockerVolumeSourcePatchArgsDict']]
    """
    flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running
    """
    gce_persistent_disk: NotRequired[Input['GCEPersistentDiskVolumeSourcePatchArgsDict']]
    """
    gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    git_repo: NotRequired[Input['GitRepoVolumeSourcePatchArgsDict']]
    """
    gitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    """
    glusterfs: NotRequired[Input['GlusterfsVolumeSourcePatchArgsDict']]
    """
    glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    """
    host_path: NotRequired[Input['HostPathVolumeSourcePatchArgsDict']]
    """
    hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    iscsi: NotRequired[Input['ISCSIVolumeSourcePatchArgsDict']]
    """
    iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
    """
    name: NotRequired[Input[str]]
    """
    name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    nfs: NotRequired[Input['NFSVolumeSourcePatchArgsDict']]
    """
    nfs represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    persistent_volume_claim: NotRequired[Input['PersistentVolumeClaimVolumeSourcePatchArgsDict']]
    """
    persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    photon_persistent_disk: NotRequired[Input['PhotonPersistentDiskVolumeSourcePatchArgsDict']]
    """
    photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    """
    portworx_volume: NotRequired[Input['PortworxVolumeSourcePatchArgsDict']]
    """
    portworxVolume represents a portworx volume attached and mounted on kubelets host machine
    """
    projected: NotRequired[Input['ProjectedVolumeSourcePatchArgsDict']]
    """
    projected items for all in one resources secrets, configmaps, and downward API
    """
    quobyte: NotRequired[Input['QuobyteVolumeSourcePatchArgsDict']]
    """
    quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    """
    rbd: NotRequired[Input['RBDVolumeSourcePatchArgsDict']]
    """
    rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    """
    scale_io: NotRequired[Input['ScaleIOVolumeSourcePatchArgsDict']]
    """
    scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    """
    secret: NotRequired[Input['SecretVolumeSourcePatchArgsDict']]
    """
    secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    """
    storageos: NotRequired[Input['StorageOSVolumeSourcePatchArgsDict']]
    """
    storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
    """
    vsphere_volume: NotRequired[Input['VsphereVirtualDiskVolumeSourcePatchArgsDict']]
    """
    vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    """

class VolumeProjectionPatchArgsDict(TypedDict):
    """
    Projection that may be projected along with other supported volume types
    """
    cluster_trust_bundle: NotRequired[Input['ClusterTrustBundleProjectionPatchArgsDict']]
    """
    ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of ClusterTrustBundle objects in an auto-updating file.

    Alpha, gated by the ClusterTrustBundleProjection feature gate.

    ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.

    Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem.  Esoteric PEM features such as inter-block comments and block headers are stripped.  Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time.
    """
    config_map: NotRequired[Input['ConfigMapProjectionPatchArgsDict']]
    """
    configMap information about the configMap data to project
    """
    downward_api: NotRequired[Input['DownwardAPIProjectionPatchArgsDict']]
    """
    downwardAPI information about the downwardAPI data to project
    """
    secret: NotRequired[Input['SecretProjectionPatchArgsDict']]
    """
    secret information about the secret data to project
    """
    service_account_token: NotRequired[Input['ServiceAccountTokenProjectionPatchArgsDict']]
    """
    serviceAccountToken is information about the serviceAccountToken data to project
    """

class VolumeProjectionArgsDict(TypedDict):
    """
    Projection that may be projected along with other supported volume types
    """
    cluster_trust_bundle: NotRequired[Input['ClusterTrustBundleProjectionArgsDict']]
    """
    ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of ClusterTrustBundle objects in an auto-updating file.

    Alpha, gated by the ClusterTrustBundleProjection feature gate.

    ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.

    Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem.  Esoteric PEM features such as inter-block comments and block headers are stripped.  Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time.
    """
    config_map: NotRequired[Input['ConfigMapProjectionArgsDict']]
    """
    configMap information about the configMap data to project
    """
    downward_api: NotRequired[Input['DownwardAPIProjectionArgsDict']]
    """
    downwardAPI information about the downwardAPI data to project
    """
    secret: NotRequired[Input['SecretProjectionArgsDict']]
    """
    secret information about the secret data to project
    """
    service_account_token: NotRequired[Input['ServiceAccountTokenProjectionArgsDict']]
    """
    serviceAccountToken is information about the serviceAccountToken data to project
    """

class VolumeResourceRequirementsPatchArgsDict(TypedDict):
    """
    VolumeResourceRequirements describes the storage resource requirements for a volume.
    """
    limits: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """
    requests: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """

class VolumeResourceRequirementsArgsDict(TypedDict):
    """
    VolumeResourceRequirements describes the storage resource requirements for a volume.
    """
    limits: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """
    requests: NotRequired[Input[Mapping[str, Input[str]]]]
    """
    Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
    """

class VolumeArgsDict(TypedDict):
    """
    Volume represents a named volume in a pod that may be accessed by any container in the pod.
    """
    name: Input[str]
    """
    name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """
    aws_elastic_block_store: NotRequired[Input['AWSElasticBlockStoreVolumeSourceArgsDict']]
    """
    awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore
    """
    azure_disk: NotRequired[Input['AzureDiskVolumeSourceArgsDict']]
    """
    azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
    """
    azure_file: NotRequired[Input['AzureFileVolumeSourceArgsDict']]
    """
    azureFile represents an Azure File Service mount on the host and bind mount to the pod.
    """
    cephfs: NotRequired[Input['CephFSVolumeSourceArgsDict']]
    """
    cephFS represents a Ceph FS mount on the host that shares a pod's lifetime
    """
    cinder: NotRequired[Input['CinderVolumeSourceArgsDict']]
    """
    cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md
    """
    config_map: NotRequired[Input['ConfigMapVolumeSourceArgsDict']]
    """
    configMap represents a configMap that should populate this volume
    """
    csi: NotRequired[Input['CSIVolumeSourceArgsDict']]
    """
    csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers (Beta feature).
    """
    downward_api: NotRequired[Input['DownwardAPIVolumeSourceArgsDict']]
    """
    downwardAPI represents downward API about the pod that should populate this volume
    """
    empty_dir: NotRequired[Input['EmptyDirVolumeSourceArgsDict']]
    """
    emptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir
    """
    ephemeral: NotRequired[Input['EphemeralVolumeSourceArgsDict']]
    """
    ephemeral represents a volume that is handled by a cluster storage driver. The volume's lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.

    Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity
       tracking are needed,
    c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through
       a PersistentVolumeClaim (see EphemeralVolumeSource for more
       information on the connection between this volume type
       and PersistentVolumeClaim).

    Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.

    Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.

    A pod can use both types of ephemeral volumes and persistent volumes at the same time.
    """
    fc: NotRequired[Input['FCVolumeSourceArgsDict']]
    """
    fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.
    """
    flex_volume: NotRequired[Input['FlexVolumeSourceArgsDict']]
    """
    flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.
    """
    flocker: NotRequired[Input['FlockerVolumeSourceArgsDict']]
    """
    flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running
    """
    gce_persistent_disk: NotRequired[Input['GCEPersistentDiskVolumeSourceArgsDict']]
    """
    gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk
    """
    git_repo: NotRequired[Input['GitRepoVolumeSourceArgsDict']]
    """
    gitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    """
    glusterfs: NotRequired[Input['GlusterfsVolumeSourceArgsDict']]
    """
    glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md
    """
    host_path: NotRequired[Input['HostPathVolumeSourceArgsDict']]
    """
    hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath
    """
    iscsi: NotRequired[Input['ISCSIVolumeSourceArgsDict']]
    """
    iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md
    """
    nfs: NotRequired[Input['NFSVolumeSourceArgsDict']]
    """
    nfs represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs
    """
    persistent_volume_claim: NotRequired[Input['PersistentVolumeClaimVolumeSourceArgsDict']]
    """
    persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
    """
    photon_persistent_disk: NotRequired[Input['PhotonPersistentDiskVolumeSourceArgsDict']]
    """
    photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine
    """
    portworx_volume: NotRequired[Input['PortworxVolumeSourceArgsDict']]
    """
    portworxVolume represents a portworx volume attached and mounted on kubelets host machine
    """
    projected: NotRequired[Input['ProjectedVolumeSourceArgsDict']]
    """
    projected items for all in one resources secrets, configmaps, and downward API
    """
    quobyte: NotRequired[Input['QuobyteVolumeSourceArgsDict']]
    """
    quobyte represents a Quobyte mount on the host that shares a pod's lifetime
    """
    rbd: NotRequired[Input['RBDVolumeSourceArgsDict']]
    """
    rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md
    """
    scale_io: NotRequired[Input['ScaleIOVolumeSourceArgsDict']]
    """
    scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
    """
    secret: NotRequired[Input['SecretVolumeSourceArgsDict']]
    """
    secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret
    """
    storageos: NotRequired[Input['StorageOSVolumeSourceArgsDict']]
    """
    storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
    """
    vsphere_volume: NotRequired[Input['VsphereVirtualDiskVolumeSourceArgsDict']]
    """
    vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine
    """

class VsphereVirtualDiskVolumeSourcePatchArgsDict(TypedDict):
    """
    Represents a vSphere volume resource.
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    storage_policy_id: NotRequired[Input[str]]
    """
    storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.
    """
    storage_policy_name: NotRequired[Input[str]]
    """
    storagePolicyName is the storage Policy Based Management (SPBM) profile name.
    """
    volume_path: NotRequired[Input[str]]
    """
    volumePath is the path that identifies vSphere volume vmdk
    """

class VsphereVirtualDiskVolumeSourceArgsDict(TypedDict):
    """
    Represents a vSphere volume resource.
    """
    volume_path: Input[str]
    """
    volumePath is the path that identifies vSphere volume vmdk
    """
    fs_type: NotRequired[Input[str]]
    """
    fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.
    """
    storage_policy_id: NotRequired[Input[str]]
    """
    storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.
    """
    storage_policy_name: NotRequired[Input[str]]
    """
    storagePolicyName is the storage Policy Based Management (SPBM) profile name.
    """

class WeightedPodAffinityTermPatchArgsDict(TypedDict):
    """
    The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)
    """
    pod_affinity_term: NotRequired[Input['PodAffinityTermPatchArgsDict']]
    """
    Required. A pod affinity term, associated with the corresponding weight.
    """
    weight: NotRequired[Input[int]]
    """
    weight associated with matching the corresponding podAffinityTerm, in the range 1-100.
    """

class WeightedPodAffinityTermArgsDict(TypedDict):
    """
    The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)
    """
    pod_affinity_term: Input['PodAffinityTermArgsDict']
    """
    Required. A pod affinity term, associated with the corresponding weight.
    """
    weight: Input[int]
    """
    weight associated with matching the corresponding podAffinityTerm, in the range 1-100.
    """

class WindowsSecurityContextOptionsPatchArgsDict(TypedDict):
    """
    WindowsSecurityContextOptions contain Windows-specific options and credentials.
    """
    gmsa_credential_spec: NotRequired[Input[str]]
    """
    GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.
    """
    gmsa_credential_spec_name: NotRequired[Input[str]]
    """
    GMSACredentialSpecName is the name of the GMSA credential spec to use.
    """
    host_process: NotRequired[Input[bool]]
    """
    HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.
    """
    run_as_user_name: NotRequired[Input[str]]
    """
    The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """

class WindowsSecurityContextOptionsArgsDict(TypedDict):
    """
    WindowsSecurityContextOptions contain Windows-specific options and credentials.
    """
    gmsa_credential_spec: NotRequired[Input[str]]
    """
    GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.
    """
    gmsa_credential_spec_name: NotRequired[Input[str]]
    """
    GMSACredentialSpecName is the name of the GMSA credential spec to use.
    """
    host_process: NotRequired[Input[bool]]
    """
    HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.
    """
    run_as_user_name: NotRequired[Input[str]]
    """
    The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
    """


class ControllerRevisionArgsDict(TypedDict):
    """
    ControllerRevision implements an immutable snapshot of state data. Clients are responsible for serializing and deserializing the objects that contain their internal state. Once a ControllerRevision has been successfully created, it can not be updated. The API Server will fail validation of all requests that attempt to mutate the Data field. ControllerRevisions may, however, be deleted. Note that, due to its use by both the DaemonSet and StatefulSet controllers for update and rollback, this object is beta. However, it may be subject to name and representation changes in future releases, and clients should not depend on its stability. It is primarily for internal use by controllers.
    """
    revision: Input[int]
    """
    Revision indicates the revision of the state represented by Data.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    data: NotRequired[Any]
    """
    Data is the serialized representation of the state.
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """

class DaemonSetConditionArgsDict(TypedDict):
    """
    DaemonSetCondition describes the state of a DaemonSet at a certain point.
    """
    status: Input[str]
    """
    Status of the condition, one of True, False, Unknown.
    """
    type: Input[str]
    """
    Type of DaemonSet condition.
    """
    last_transition_time: NotRequired[Input[str]]
    """
    Last time the condition transitioned from one status to another.
    """
    message: NotRequired[Input[str]]
    """
    A human readable message indicating details about the transition.
    """
    reason: NotRequired[Input[str]]
    """
    The reason for the condition's last transition.
    """

class DaemonSetSpecPatchArgsDict(TypedDict):
    """
    DaemonSetSpec is the specification of a daemon set.
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).
    """
    revision_history_limit: NotRequired[Input[int]]
    """
    The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.
    """
    selector: NotRequired[Input['LabelSelectorPatchArgsDict']]
    """
    A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    """
    template: NotRequired[Input['PodTemplateSpecPatchArgsDict']]
    """
    An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template
    """
    update_strategy: NotRequired[Input['DaemonSetUpdateStrategyPatchArgsDict']]
    """
    An update strategy to replace existing DaemonSet pods with new pods.
    """

class DaemonSetSpecArgsDict(TypedDict):
    """
    DaemonSetSpec is the specification of a daemon set.
    """
    selector: Input['LabelSelectorArgsDict']
    """
    A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    """
    template: Input['PodTemplateSpecArgsDict']
    """
    An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).
    """
    revision_history_limit: NotRequired[Input[int]]
    """
    The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.
    """
    update_strategy: NotRequired[Input['DaemonSetUpdateStrategyArgsDict']]
    """
    An update strategy to replace existing DaemonSet pods with new pods.
    """

class DaemonSetStatusArgsDict(TypedDict):
    """
    DaemonSetStatus represents the current status of a daemon set.
    """
    current_number_scheduled: Input[int]
    """
    The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
    """
    desired_number_scheduled: Input[int]
    """
    The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
    """
    number_misscheduled: Input[int]
    """
    The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
    """
    number_ready: Input[int]
    """
    numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition.
    """
    collision_count: NotRequired[Input[int]]
    """
    Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.
    """
    conditions: NotRequired[Input[Sequence[Input['DaemonSetConditionArgsDict']]]]
    """
    Represents the latest available observations of a DaemonSet's current state.
    """
    number_available: NotRequired[Input[int]]
    """
    The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)
    """
    number_unavailable: NotRequired[Input[int]]
    """
    The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)
    """
    observed_generation: NotRequired[Input[int]]
    """
    The most recent generation observed by the daemon set controller.
    """
    updated_number_scheduled: NotRequired[Input[int]]
    """
    The total number of nodes that are running updated daemon pod
    """

class DaemonSetUpdateStrategyPatchArgsDict(TypedDict):
    """
    DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet.
    """
    rolling_update: NotRequired[Input['RollingUpdateDaemonSetPatchArgsDict']]
    """
    Rolling update config params. Present only if type = "RollingUpdate".
    """
    type: NotRequired[Input[str]]
    """
    Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate.
    """

class DaemonSetUpdateStrategyArgsDict(TypedDict):
    """
    DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet.
    """
    rolling_update: NotRequired[Input['RollingUpdateDaemonSetArgsDict']]
    """
    Rolling update config params. Present only if type = "RollingUpdate".
    """
    type: NotRequired[Input[str]]
    """
    Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate.
    """

class DaemonSetArgsDict(TypedDict):
    """
    DaemonSet represents the configuration of a daemon set.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['DaemonSetSpecArgsDict']]
    """
    The desired behavior of this daemon set. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    status: NotRequired[Input['DaemonSetStatusArgsDict']]
    """
    The current status of this daemon set. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class DeploymentConditionArgsDict(TypedDict):
    """
    DeploymentCondition describes the state of a deployment at a certain point.
    """
    status: Input[str]
    """
    Status of the condition, one of True, False, Unknown.
    """
    type: Input[str]
    """
    Type of deployment condition.
    """
    last_transition_time: NotRequired[Input[str]]
    """
    Last time the condition transitioned from one status to another.
    """
    last_update_time: NotRequired[Input[str]]
    """
    The last time this condition was updated.
    """
    message: NotRequired[Input[str]]
    """
    A human readable message indicating details about the transition.
    """
    reason: NotRequired[Input[str]]
    """
    The reason for the condition's last transition.
    """

class DeploymentSpecPatchArgsDict(TypedDict):
    """
    DeploymentSpec is the specification of the desired behavior of the Deployment.
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    """
    paused: NotRequired[Input[bool]]
    """
    Indicates that the deployment is paused.
    """
    progress_deadline_seconds: NotRequired[Input[int]]
    """
    The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.
    """
    replicas: NotRequired[Input[int]]
    """
    Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.
    """
    revision_history_limit: NotRequired[Input[int]]
    """
    The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.
    """
    selector: NotRequired[Input['LabelSelectorPatchArgsDict']]
    """
    Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.
    """
    strategy: NotRequired[Input['DeploymentStrategyPatchArgsDict']]
    """
    The deployment strategy to use to replace existing pods with new ones.
    """
    template: NotRequired[Input['PodTemplateSpecPatchArgsDict']]
    """
    Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always".
    """

class DeploymentSpecArgsDict(TypedDict):
    """
    DeploymentSpec is the specification of the desired behavior of the Deployment.
    """
    selector: Input['LabelSelectorArgsDict']
    """
    Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.
    """
    template: Input['PodTemplateSpecArgsDict']
    """
    Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always".
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    """
    paused: NotRequired[Input[bool]]
    """
    Indicates that the deployment is paused.
    """
    progress_deadline_seconds: NotRequired[Input[int]]
    """
    The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.
    """
    replicas: NotRequired[Input[int]]
    """
    Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.
    """
    revision_history_limit: NotRequired[Input[int]]
    """
    The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.
    """
    strategy: NotRequired[Input['DeploymentStrategyArgsDict']]
    """
    The deployment strategy to use to replace existing pods with new ones.
    """

class DeploymentStatusArgsDict(TypedDict):
    """
    DeploymentStatus is the most recently observed status of the Deployment.
    """
    available_replicas: NotRequired[Input[int]]
    """
    Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.
    """
    collision_count: NotRequired[Input[int]]
    """
    Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.
    """
    conditions: NotRequired[Input[Sequence[Input['DeploymentConditionArgsDict']]]]
    """
    Represents the latest available observations of a deployment's current state.
    """
    observed_generation: NotRequired[Input[int]]
    """
    The generation observed by the deployment controller.
    """
    ready_replicas: NotRequired[Input[int]]
    """
    readyReplicas is the number of pods targeted by this Deployment with a Ready Condition.
    """
    replicas: NotRequired[Input[int]]
    """
    Total number of non-terminated pods targeted by this deployment (their labels match the selector).
    """
    unavailable_replicas: NotRequired[Input[int]]
    """
    Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.
    """
    updated_replicas: NotRequired[Input[int]]
    """
    Total number of non-terminated pods targeted by this deployment that have the desired template spec.
    """

class DeploymentStrategyPatchArgsDict(TypedDict):
    """
    DeploymentStrategy describes how to replace existing pods with new ones.
    """
    rolling_update: NotRequired[Input['RollingUpdateDeploymentPatchArgsDict']]
    """
    Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.
    """
    type: NotRequired[Input[str]]
    """
    Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.
    """

class DeploymentStrategyArgsDict(TypedDict):
    """
    DeploymentStrategy describes how to replace existing pods with new ones.
    """
    rolling_update: NotRequired[Input['RollingUpdateDeploymentArgsDict']]
    """
    Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.
    """
    type: NotRequired[Input[str]]
    """
    Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.
    """

class DeploymentArgsDict(TypedDict):
    """
    Deployment enables declarative updates for Pods and ReplicaSets.

    This resource waits until its status is ready before registering success
    for create/update, and populating output properties from the current state of the resource.
    The following conditions are used to determine whether the resource creation has
    succeeded or failed:

    1. The Deployment has begun to be updated by the Deployment controller. If the current
       generation of the Deployment is > 1, then this means that the current generation must
       be different from the generation reported by the last outputs.
    2. There exists a ReplicaSet whose revision is equal to the current revision of the
       Deployment.
    3. The Deployment's '.status.conditions' has a status of type 'Available' whose 'status'
       member is set to 'True'.
    4. If the Deployment has generation > 1, then '.status.conditions' has a status of type
       'Progressing', whose 'status' member is set to 'True', and whose 'reason' is
       'NewReplicaSetAvailable'. For generation <= 1, this status field does not exist,
       because it doesn't do a rollout (i.e., it simply creates the Deployment and
       corresponding ReplicaSet), and therefore there is no rollout to mark as 'Progressing'.

    If the Deployment has not reached a Ready state after 10 minutes, it will
    time out and mark the resource update as Failed. You can override the default timeout value
    by setting the 'customTimeouts' option on the resource.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['DeploymentSpecArgsDict']]
    """
    Specification of the desired behavior of the Deployment.
    """
    status: NotRequired[Input['DeploymentStatusArgsDict']]
    """
    Most recently observed status of the Deployment.
    """

class ReplicaSetConditionArgsDict(TypedDict):
    """
    ReplicaSetCondition describes the state of a replica set at a certain point.
    """
    status: Input[str]
    """
    Status of the condition, one of True, False, Unknown.
    """
    type: Input[str]
    """
    Type of replica set condition.
    """
    last_transition_time: NotRequired[Input[str]]
    """
    The last time the condition transitioned from one status to another.
    """
    message: NotRequired[Input[str]]
    """
    A human readable message indicating details about the transition.
    """
    reason: NotRequired[Input[str]]
    """
    The reason for the condition's last transition.
    """

class ReplicaSetSpecPatchArgsDict(TypedDict):
    """
    ReplicaSetSpec is the specification of a ReplicaSet.
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    """
    replicas: NotRequired[Input[int]]
    """
    Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller
    """
    selector: NotRequired[Input['LabelSelectorPatchArgsDict']]
    """
    Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    """
    template: NotRequired[Input['PodTemplateSpecPatchArgsDict']]
    """
    Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template
    """

class ReplicaSetSpecArgsDict(TypedDict):
    """
    ReplicaSetSpec is the specification of a ReplicaSet.
    """
    selector: Input['LabelSelectorArgsDict']
    """
    Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    """
    replicas: NotRequired[Input[int]]
    """
    Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller
    """
    template: NotRequired[Input['PodTemplateSpecArgsDict']]
    """
    Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template
    """

class ReplicaSetStatusArgsDict(TypedDict):
    """
    ReplicaSetStatus represents the current status of a ReplicaSet.
    """
    replicas: Input[int]
    """
    Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller
    """
    available_replicas: NotRequired[Input[int]]
    """
    The number of available replicas (ready for at least minReadySeconds) for this replica set.
    """
    conditions: NotRequired[Input[Sequence[Input['ReplicaSetConditionArgsDict']]]]
    """
    Represents the latest available observations of a replica set's current state.
    """
    fully_labeled_replicas: NotRequired[Input[int]]
    """
    The number of pods that have labels matching the labels of the pod template of the replicaset.
    """
    observed_generation: NotRequired[Input[int]]
    """
    ObservedGeneration reflects the generation of the most recently observed ReplicaSet.
    """
    ready_replicas: NotRequired[Input[int]]
    """
    readyReplicas is the number of pods targeted by this ReplicaSet with a Ready Condition.
    """

class ReplicaSetArgsDict(TypedDict):
    """
    ReplicaSet ensures that a specified number of pod replicas are running at any given time.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['ReplicaSetSpecArgsDict']]
    """
    Spec defines the specification of the desired behavior of the ReplicaSet. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    status: NotRequired[Input['ReplicaSetStatusArgsDict']]
    """
    Status is the most recently observed status of the ReplicaSet. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """

class RollingUpdateDaemonSetPatchArgsDict(TypedDict):
    """
    Spec to control the desired behavior of daemon set rolling update.
    """
    max_surge: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of nodes with an existing available DaemonSet pod that can have an updated DaemonSet pod during during an update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up to a minimum of 1. Default value is 0. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their a new pod created before the old pod is marked as deleted. The update starts by launching new pods on 30% of nodes. Once an updated pod is available (Ready for at least minReadySeconds) the old DaemonSet pod on that node is marked deleted. If the old pod becomes unavailable for any reason (Ready transitions to false, is evicted, or is drained) an updated pod is immediatedly created on that node without considering surge limits. Allowing surge implies the possibility that the resources consumed by the daemonset on any given node can double if the readiness check fails, and so resource intensive daemonsets should take into account that they may cause evictions during disruption.
    """
    max_unavailable: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of DaemonSet pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot be 0 if MaxSurge is 0 Default value is 1. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their pods stopped for an update at any given time. The update starts by stopping at most 30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are available at all times during the update.
    """

class RollingUpdateDaemonSetArgsDict(TypedDict):
    """
    Spec to control the desired behavior of daemon set rolling update.
    """
    max_surge: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of nodes with an existing available DaemonSet pod that can have an updated DaemonSet pod during during an update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up to a minimum of 1. Default value is 0. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their a new pod created before the old pod is marked as deleted. The update starts by launching new pods on 30% of nodes. Once an updated pod is available (Ready for at least minReadySeconds) the old DaemonSet pod on that node is marked deleted. If the old pod becomes unavailable for any reason (Ready transitions to false, is evicted, or is drained) an updated pod is immediatedly created on that node without considering surge limits. Allowing surge implies the possibility that the resources consumed by the daemonset on any given node can double if the readiness check fails, and so resource intensive daemonsets should take into account that they may cause evictions during disruption.
    """
    max_unavailable: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of DaemonSet pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot be 0 if MaxSurge is 0 Default value is 1. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their pods stopped for an update at any given time. The update starts by stopping at most 30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are available at all times during the update.
    """

class RollingUpdateDeploymentPatchArgsDict(TypedDict):
    """
    Spec to control the desired behavior of rolling update.
    """
    max_surge: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.
    """
    max_unavailable: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.
    """

class RollingUpdateDeploymentArgsDict(TypedDict):
    """
    Spec to control the desired behavior of rolling update.
    """
    max_surge: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.
    """
    max_unavailable: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.
    """

class RollingUpdateStatefulSetStrategyPatchArgsDict(TypedDict):
    """
    RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType.
    """
    max_unavailable: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable.
    """
    partition: NotRequired[Input[int]]
    """
    Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0.
    """

class RollingUpdateStatefulSetStrategyArgsDict(TypedDict):
    """
    RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType.
    """
    max_unavailable: NotRequired[Input[Union[int, str]]]
    """
    The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable.
    """
    partition: NotRequired[Input[int]]
    """
    Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0.
    """

class StatefulSetConditionArgsDict(TypedDict):
    """
    StatefulSetCondition describes the state of a statefulset at a certain point.
    """
    status: Input[str]
    """
    Status of the condition, one of True, False, Unknown.
    """
    type: Input[str]
    """
    Type of statefulset condition.
    """
    last_transition_time: NotRequired[Input[str]]
    """
    Last time the condition transitioned from one status to another.
    """
    message: NotRequired[Input[str]]
    """
    A human readable message indicating details about the transition.
    """
    reason: NotRequired[Input[str]]
    """
    The reason for the condition's last transition.
    """

class StatefulSetOrdinalsPatchArgsDict(TypedDict):
    """
    StatefulSetOrdinals describes the policy used for replica ordinal assignment in this StatefulSet.
    """
    start: NotRequired[Input[int]]
    """
    start is the number representing the first replica's index. It may be used to number replicas from an alternate index (eg: 1-indexed) over the default 0-indexed names, or to orchestrate progressive movement of replicas from one StatefulSet to another. If set, replica indices will be in the range:
      [.spec.ordinals.start, .spec.ordinals.start + .spec.replicas).
    If unset, defaults to 0. Replica indices will be in the range:
      [0, .spec.replicas).
    """

class StatefulSetOrdinalsArgsDict(TypedDict):
    """
    StatefulSetOrdinals describes the policy used for replica ordinal assignment in this StatefulSet.
    """
    start: NotRequired[Input[int]]
    """
    start is the number representing the first replica's index. It may be used to number replicas from an alternate index (eg: 1-indexed) over the default 0-indexed names, or to orchestrate progressive movement of replicas from one StatefulSet to another. If set, replica indices will be in the range:
      [.spec.ordinals.start, .spec.ordinals.start + .spec.replicas).
    If unset, defaults to 0. Replica indices will be in the range:
      [0, .spec.replicas).
    """

class StatefulSetPersistentVolumeClaimRetentionPolicyPatchArgsDict(TypedDict):
    """
    StatefulSetPersistentVolumeClaimRetentionPolicy describes the policy used for PVCs created from the StatefulSet VolumeClaimTemplates.
    """
    when_deleted: NotRequired[Input[str]]
    """
    WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted.
    """
    when_scaled: NotRequired[Input[str]]
    """
    WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the replica count to be deleted.
    """

class StatefulSetPersistentVolumeClaimRetentionPolicyArgsDict(TypedDict):
    """
    StatefulSetPersistentVolumeClaimRetentionPolicy describes the policy used for PVCs created from the StatefulSet VolumeClaimTemplates.
    """
    when_deleted: NotRequired[Input[str]]
    """
    WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted.
    """
    when_scaled: NotRequired[Input[str]]
    """
    WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the replica count to be deleted.
    """

class StatefulSetSpecPatchArgsDict(TypedDict):
    """
    A StatefulSetSpec is the specification of a StatefulSet.
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    """
    ordinals: NotRequired[Input['StatefulSetOrdinalsPatchArgsDict']]
    """
    ordinals controls the numbering of replica indices in a StatefulSet. The default ordinals behavior assigns a "0" index to the first replica and increments the index by one for each additional replica requested. Using the ordinals field requires the StatefulSetStartOrdinal feature gate to be enabled, which is beta.
    """
    persistent_volume_claim_retention_policy: NotRequired[Input['StatefulSetPersistentVolumeClaimRetentionPolicyPatchArgsDict']]
    """
    persistentVolumeClaimRetentionPolicy describes the lifecycle of persistent volume claims created from volumeClaimTemplates. By default, all persistent volume claims are created as needed and retained until manually deleted. This policy allows the lifecycle to be altered, for example by deleting persistent volume claims when their stateful set is deleted, or when their pod is scaled down. This requires the StatefulSetAutoDeletePVC feature gate to be enabled, which is alpha.  +optional
    """
    pod_management_policy: NotRequired[Input[str]]
    """
    podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.
    """
    replicas: NotRequired[Input[int]]
    """
    replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.
    """
    revision_history_limit: NotRequired[Input[int]]
    """
    revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.
    """
    selector: NotRequired[Input['LabelSelectorPatchArgsDict']]
    """
    selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    """
    service_name: NotRequired[Input[str]]
    """
    serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller.
    """
    template: NotRequired[Input['PodTemplateSpecPatchArgsDict']]
    """
    template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet. Each pod will be named with the format <statefulsetname>-<podindex>. For example, a pod in a StatefulSet named "web" with index number "3" would be named "web-3". The only allowed template.spec.restartPolicy value is "Always".
    """
    update_strategy: NotRequired[Input['StatefulSetUpdateStrategyPatchArgsDict']]
    """
    updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.
    """
    volume_claim_templates: NotRequired[Input[Sequence[Input['PersistentVolumeClaimPatchArgsDict']]]]
    """
    volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.
    """

class StatefulSetSpecArgsDict(TypedDict):
    """
    A StatefulSetSpec is the specification of a StatefulSet.
    """
    selector: Input['LabelSelectorArgsDict']
    """
    selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
    """
    service_name: Input[str]
    """
    serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller.
    """
    template: Input['PodTemplateSpecArgsDict']
    """
    template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet. Each pod will be named with the format <statefulsetname>-<podindex>. For example, a pod in a StatefulSet named "web" with index number "3" would be named "web-3". The only allowed template.spec.restartPolicy value is "Always".
    """
    min_ready_seconds: NotRequired[Input[int]]
    """
    Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)
    """
    ordinals: NotRequired[Input['StatefulSetOrdinalsArgsDict']]
    """
    ordinals controls the numbering of replica indices in a StatefulSet. The default ordinals behavior assigns a "0" index to the first replica and increments the index by one for each additional replica requested. Using the ordinals field requires the StatefulSetStartOrdinal feature gate to be enabled, which is beta.
    """
    persistent_volume_claim_retention_policy: NotRequired[Input['StatefulSetPersistentVolumeClaimRetentionPolicyArgsDict']]
    """
    persistentVolumeClaimRetentionPolicy describes the lifecycle of persistent volume claims created from volumeClaimTemplates. By default, all persistent volume claims are created as needed and retained until manually deleted. This policy allows the lifecycle to be altered, for example by deleting persistent volume claims when their stateful set is deleted, or when their pod is scaled down. This requires the StatefulSetAutoDeletePVC feature gate to be enabled, which is alpha.  +optional
    """
    pod_management_policy: NotRequired[Input[str]]
    """
    podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.
    """
    replicas: NotRequired[Input[int]]
    """
    replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.
    """
    revision_history_limit: NotRequired[Input[int]]
    """
    revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.
    """
    update_strategy: NotRequired[Input['StatefulSetUpdateStrategyArgsDict']]
    """
    updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.
    """
    volume_claim_templates: NotRequired[Input[Sequence[Input['PersistentVolumeClaimArgsDict']]]]
    """
    volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.
    """

class StatefulSetStatusArgsDict(TypedDict):
    """
    StatefulSetStatus represents the current state of a StatefulSet.
    """
    replicas: Input[int]
    """
    replicas is the number of Pods created by the StatefulSet controller.
    """
    available_replicas: NotRequired[Input[int]]
    """
    Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset.
    """
    collision_count: NotRequired[Input[int]]
    """
    collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.
    """
    conditions: NotRequired[Input[Sequence[Input['StatefulSetConditionArgsDict']]]]
    """
    Represents the latest available observations of a statefulset's current state.
    """
    current_replicas: NotRequired[Input[int]]
    """
    currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.
    """
    current_revision: NotRequired[Input[str]]
    """
    currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).
    """
    observed_generation: NotRequired[Input[int]]
    """
    observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.
    """
    ready_replicas: NotRequired[Input[int]]
    """
    readyReplicas is the number of pods created for this StatefulSet with a Ready Condition.
    """
    update_revision: NotRequired[Input[str]]
    """
    updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)
    """
    updated_replicas: NotRequired[Input[int]]
    """
    updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.
    """

class StatefulSetUpdateStrategyPatchArgsDict(TypedDict):
    """
    StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy.
    """
    rolling_update: NotRequired[Input['RollingUpdateStatefulSetStrategyPatchArgsDict']]
    """
    RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType.
    """
    type: NotRequired[Input[str]]
    """
    Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.
    """

class StatefulSetUpdateStrategyArgsDict(TypedDict):
    """
    StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy.
    """
    rolling_update: NotRequired[Input['RollingUpdateStatefulSetStrategyArgsDict']]
    """
    RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType.
    """
    type: NotRequired[Input[str]]
    """
    Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.
    """

class StatefulSetArgsDict(TypedDict):
    """
    StatefulSet represents a set of pods with consistent identities. Identities are defined as:
      - Network: A single stable DNS and hostname.
      - Storage: As many VolumeClaims as requested.

    The StatefulSet guarantees that a given network identity will always map to the same storage identity.

    This resource waits until its status is ready before registering success
    for create/update, and populating output properties from the current state of the resource.
    The following conditions are used to determine whether the resource creation has
    succeeded or failed:

    1. The value of 'spec.replicas' matches '.status.replicas', '.status.currentReplicas',
       and '.status.readyReplicas'.
    2. The value of '.status.updateRevision' matches '.status.currentRevision'.

    If the StatefulSet has not reached a Ready state after 10 minutes, it will
    time out and mark the resource update as Failed. You can override the default timeout value
    by setting the 'customTimeouts' option on the resource.
    """
    api_version: NotRequired[Input[str]]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: NotRequired[Input[str]]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: NotRequired[Input['ObjectMetaArgsDict']]
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: NotRequired[Input['StatefulSetSpecArgsDict']]
    """
    Spec defines the desired identities of pods in this set.
    """
    status: NotRequired[Input['StatefulSetStatusArgsDict']]
    """
    Status is the current status of Pods in this StatefulSet. This data may be out of date by some window of time.
    """


class ServiceSpecType(str, Enum):
    EXTERNAL_NAME = "ExternalName"
    CLUSTER_IP = "ClusterIP"
    NODE_PORT = "NodePort"
    LOAD_BALANCER = "LoadBalancer"
