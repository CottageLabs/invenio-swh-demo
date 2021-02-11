from invenio_rdm_records.services.config import RDMRecordServiceConfig

from invenio_swh.components import InvenioSWHComponent


class RDMWithSWHRecordServiceConfig(RDMRecordServiceConfig):
    components = [
        *RDMRecordServiceConfig.components,
        InvenioSWHComponent,
    ]
