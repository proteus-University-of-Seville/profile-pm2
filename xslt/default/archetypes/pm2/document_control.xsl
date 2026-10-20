<?xml version="1.0" encoding="utf-8"?>

<!-- ======================================================== -->
<!-- File    : document_control.xsl                           -->
<!-- Content : PM2 XSLT for the document control block        -->
<!-- Author  : Amador Durán Toro & Claude Code                -->
<!-- Date    : 2026/10/19                                     -->
<!-- Version : 1.0                                            -->
<!-- ======================================================== -->
<!-- Renders the "document control" pages of the PM2          -->
<!-- templates: the control information of the document it    -->
<!-- belongs to (the Project Owner comes from the initiation  -->
<!-- request of the document, if any), its approvers and      -->
<!-- reviewers, its history (latest revision first) and its   -->
<!-- location.                                                -->
<!-- ======================================================== -->

<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:proteus="http://proteus.us.es"
  xmlns:proteus-utils="http://proteus.us.es/utils"
  exclude-result-prefixes="proteus proteus-utils"
>

  <!-- A row of the control information table: label and content -->
  <xsl:template name="document_control_row">
    <xsl:param name="label"/>
    <xsl:param name="content"/>
    <tr>
      <th><xsl:value-of select="$label"/></th>
      <td><xsl:copy-of select="$content"/></td>
    </tr>
  </xsl:template>

  <!-- ================================================================== -->
  <!-- document-control template                                          -->
  <!-- ================================================================== -->

  <xsl:template
    match="object[contains(concat(' ', normalize-space(@classes), ' '),' document-control ')]"
    name="document_control_template"
    priority="1"
  >
    <xsl:variable name="document"
      select="ancestor::object[contains(concat(' ', normalize-space(@classes), ' '), ' :Proteus-document ')][1]"/>
    <xsl:variable name="request"
      select="$document//object[contains(concat(' ', normalize-space(@classes), ' '), ' initiation-request ')][1]"/>
    <xsl:variable name="approvals"
      select="children/object[contains(concat(' ', normalize-space(@classes), ' '), ' approval ')]"/>
    <xsl:variable name="revisions"
      select="children/object[contains(concat(' ', normalize-space(@classes), ' '), ' revision ')]"/>
    <xsl:variable name="location"
      select="normalize-space($document/properties/*[@name='document-location'])"/>

    <div id="{@id}" data-proteus-id="{@id}" class="proteus_object document_control">

      <h2 class="document_control_title">
        <xsl:value-of select="properties/*[@name=':Proteus-name']"/>
      </h2>

      <!-- Control information of the document -->
      <table class="document_control_table">
        <caption><xsl:value-of select="proteus-utils:i18n('xslt.document_control_info')"/></caption>
        <tbody>
          <xsl:call-template name="document_control_row">
            <xsl:with-param name="label" select="proteus-utils:i18n('xslt.document_title')"/>
            <xsl:with-param name="content" select="string($document/properties/*[@name=':Proteus-name'])"/>
          </xsl:call-template>
          <xsl:call-template name="document_control_row">
            <xsl:with-param name="label" select="proteus-utils:i18n('xslt.project_title')"/>
            <xsl:with-param name="content" select="string($document/parent::*/parent::*/properties/*[@name=':Proteus-name'])"/>
          </xsl:call-template>
          <xsl:call-template name="document_control_row">
            <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.document-author')"/>
            <xsl:with-param name="content">
              <xsl:apply-templates select="$document/properties/traceProperty[@name='document-author']" mode="paragraph"/>
            </xsl:with-param>
          </xsl:call-template>
          <xsl:if test="$request">
            <xsl:call-template name="document_control_row">
              <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.project-owner')"/>
              <xsl:with-param name="content">
                <xsl:apply-templates select="$request/properties/traceProperty[@name='project-owner']" mode="paragraph"/>
              </xsl:with-param>
            </xsl:call-template>
          </xsl:if>
          <xsl:call-template name="document_control_row">
            <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.project-manager')"/>
            <xsl:with-param name="content">
              <xsl:apply-templates select="$document/properties/traceProperty[@name='project-manager']" mode="paragraph"/>
            </xsl:with-param>
          </xsl:call-template>
          <xsl:call-template name="document_control_row">
            <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.version')"/>
            <xsl:with-param name="content" select="string($document/properties/*[@name='version'])"/>
          </xsl:call-template>
          <xsl:call-template name="document_control_row">
            <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.sensitivity')"/>
            <xsl:with-param name="content">
              <xsl:apply-templates select="$document/properties/enumProperty[@name='sensitivity']"/>
            </xsl:with-param>
          </xsl:call-template>
          <xsl:call-template name="document_control_row">
            <xsl:with-param name="label" select="proteus-utils:i18n('xslt.date')"/>
            <xsl:with-param name="content" select="string($document/properties/*[@name=':Proteus-date'])"/>
          </xsl:call-template>
        </tbody>
      </table>

      <!-- Approvers and reviewers -->
      <xsl:if test="$approvals">
        <table class="document_control_table document_control_list">
          <caption><xsl:value-of select="proteus-utils:i18n('xslt.approvers_reviewers')"/></caption>
          <thead>
            <tr>
              <th><xsl:value-of select="proteus-utils:i18n('xslt.name')"/></th>
              <th><xsl:value-of select="proteus-utils:i18n('xslt.role')"/></th>
              <th><xsl:value-of select="proteus-utils:i18n('archetype.prop_name.action')"/></th>
              <th><xsl:value-of select="proteus-utils:i18n('xslt.date')"/></th>
            </tr>
          </thead>
          <tbody>
            <xsl:for-each select="$approvals">
              <xsl:variable name="approver"
                select="//object[@id = current()/properties/traceProperty[@name='approver']/trace[1]/@target]"/>
              <tr id="{@id}" data-proteus-id="{@id}">
                <td>
                  <xsl:if test="$approver">
                    <xsl:call-template name="trace_target_link">
                      <xsl:with-param name="target_object" select="$approver"/>
                    </xsl:call-template>
                  </xsl:if>
                </td>
                <td><xsl:value-of select="$approver/properties/*[@name='role']"/></td>
                <td><xsl:apply-templates select="properties/enumProperty[@name='action']"/></td>
                <td class="date"><xsl:value-of select="properties/*[@name=':Proteus-date']"/></td>
              </tr>
            </xsl:for-each>
          </tbody>
        </table>
      </xsl:if>

      <!-- History, latest revision first -->
      <xsl:if test="$revisions">
        <table class="document_control_table document_control_list">
          <caption><xsl:value-of select="proteus-utils:i18n('xslt.document_history')"/></caption>
          <thead>
            <tr>
              <th><xsl:value-of select="proteus-utils:i18n('archetype.prop_name.revision')"/></th>
              <th><xsl:value-of select="proteus-utils:i18n('xslt.date')"/></th>
              <th><xsl:value-of select="proteus-utils:i18n('archetype.prop_name.created-by')"/></th>
              <th><xsl:value-of select="proteus-utils:i18n('archetype.prop_name.changes')"/></th>
            </tr>
          </thead>
          <tbody>
            <xsl:for-each select="$revisions">
              <xsl:sort select="properties/*[@name=':Proteus-date']" order="descending"/>
              <xsl:sort select="properties/*[@name='revision']" order="descending"/>
              <tr id="{@id}" data-proteus-id="{@id}">
                <td><xsl:value-of select="properties/*[@name='revision']"/></td>
                <td class="date"><xsl:value-of select="properties/*[@name=':Proteus-date']"/></td>
                <td><xsl:apply-templates select="properties/traceProperty[@name='created-by']" mode="paragraph"/></td>
                <td>
                  <xsl:call-template name="generate_markdown">
                    <xsl:with-param name="content" select="properties/*[@name='changes']"/>
                  </xsl:call-template>
                </td>
              </tr>
            </xsl:for-each>
          </tbody>
        </table>
      </xsl:if>

      <!-- Location of the document -->
      <xsl:if test="$location != ''">
        <p class="document_location">
          <xsl:value-of select="proteus-utils:i18n('xslt.document_location', $location)"/>
        </p>
      </xsl:if>

    </div>
  </xsl:template>

</xsl:stylesheet>
