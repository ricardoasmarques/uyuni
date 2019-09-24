// @flow
import React from 'react';
import {LinkButton} from "components/buttons";

import styles from "./filters-project.css"
import {showErrorToastr, showSuccessToastr} from "components/toastr/toastr";
import useLifecycleActionsApi from "../../../api/use-lifecycle-actions-api";
import CreatorPanel from "components/panels/CreatorPanel";
import type {ProjectFilterServerType} from "../../../type/project.type";
import FiltersProjectSelection from "./filters-project-selection";
import statesEnum from "../../../business/states.enum";
import {getClmFilterDescription} from "../../../business/filters.enum";
import useRoles from "core/auth/use-roles";
import {isOrgAdmin} from "core/auth/auth.utils";

type FiltersProps = {
  projectId: string,
  selectedFilters: Array<ProjectFilterServerType>,
  onChange: Function,
};

const renderFilterEntry = (filter, projectId, symbol, last) => {
  const descr = getClmFilterDescription(filter);
  const filterButton =
    <div className={styles.icon_wrapper_vertical_center}>
      <LinkButton
        id={`edit-filter-${filter.id}`}
        icon='fa-edit'
        title={t(`Edit Filter ${filter.name}`)}
        className='pull-right js-spa'
        href={`/rhn/manager/contentmanagement/filters?openFilterId=${filter.id}&projectLabel=${projectId}`}
      />
    </div>;

  let filterClassName;
  let filterIconName;

  if (filter.state === statesEnum.enum.ATTACHED.key) {
    filterClassName = `text-success`;
    filterIconName = 'fa-plus';
  }
  else if (filter.state === statesEnum.enum.EDITED.key) {
    filterClassName = `text-warning`;
    filterIconName = 'fa-edit';
  }
  else if (filter.state === statesEnum.enum.DETACHED.key) {
    filterClassName = `text-danger ${styles.dettached}`;
    filterIconName = 'fa-minus';
  }
  else {
    filterClassName = `${styles.wrapper}`;
  }

  return (
    <>
      <li
        key={`filter_list_item_${filter.id}`}
        className={`list-group-item ${styles.wrapper} ${filterClassName}`}>
        {filterIconName && <i class={`fa ${filterIconName}`}></i>}
        {descr}
        {filterButton}
      </li>
      {!last && <div style={{margin: "4px"}} className="row text-center">{symbol}</div>}
    </>
  );
}

const FiltersProject = (props:  FiltersProps) => {

  const {onAction, cancelAction, isLoading} = useLifecycleActionsApi({
    resource: 'projects', nestedResource: "filters"
  });
  const roles = useRoles();
  const hasEditingPermissions = isOrgAdmin(roles);

  const displayingFilters = [...props.selectedFilters];
  displayingFilters.sort((a, b) => a.name.toLowerCase().localeCompare(b.name.toLowerCase()));

  const allowFilters = displayingFilters.filter(filter => filter.rule === "allow");
  const denyFilters = displayingFilters.filter(filter => filter.rule === "deny");

  return (

    <CreatorPanel
      id="filters"
      title={t('Filters')}
      creatingText="Attach/Detach Filters"
      panelLevel="2"
      collapsible
      customIconClass="fa-small"
      disableEditing={!hasEditingPermissions}
      onCancel={() => cancelAction()}
      onOpen={({setItem}) => setItem(props.selectedFilters.map(filter => filter.id))}
      onSave={({closeDialog, item}) => {
        const requestParam = {
          projectLabel: props.projectId,
          filtersIds: item,
        };

        onAction(requestParam, "update", props.projectId)
          .then((projectWithUpdatedSources) => {
            closeDialog();
            showSuccessToastr(t("Filters edited successfully"));
            props.onChange(projectWithUpdatedSources)
          })
          .catch((error) => {
            showErrorToastr(error, {autoHide: false});
          });
      }}
      renderCreationContent={({setItem}) => {
        return (
          <FiltersProjectSelection
            isUpdatingFilter={isLoading}
            projectId={props.projectId}
            initialSelectedFiltersIds={
              props.selectedFilters
                .filter(filter => !statesEnum.isDeletion(filter.state))
                .map(filter => filter.id)
            }
            onChange={setItem}
          />
        )
      }}
      renderContent={() =>
        <div className="min-height-panel">
          <div className="col-md-6">
            {
              denyFilters.length > 0 &&
              <>
                <h4>{t("Deny")} <small>{t("filter out")}</small></h4>
                <ul className="list-group">
                  {
                    denyFilters.map((filter, index) => renderFilterEntry(filter, props.projectId,
                      <i class="fa fa-filter"/>, index === denyFilters.length - 1))
                  }
                </ul>
              </>
            }
          </div>

          <div className="col-md-6">
            {
              allowFilters.length > 0 &&
                <>
                  <h4>{t("Allow")} <small>{t("select from the full source even if you have excluded them before with deny")}</small>
                  </h4>
                  <ul className="list-group">
                    {
                      allowFilters.map((filter, index) => renderFilterEntry(filter, props.projectId,
                        <i className="fa fa-plus-circle"/>, index === allowFilters.length - 1))
                    }
                  </ul>
                </>
            }
          </div>
        </div>
      }
    />

  );
};

export default FiltersProject;
