<?xml version="1.0" encoding="utf-8"?>

<!-- ======================================================== -->
<!-- File    : document_control.xsl                           -->
<!-- Content : PM2 LaTeX XSLT for the document control block  -->
<!-- Author  : Amador Durán Toro & Claude Code                -->
<!-- Date    : 2026/10/19                                     -->
<!-- Version : 1.0                                            -->
<!-- ======================================================== -->
<!-- A card with the control information of the document it  -->
<!-- belongs to (the Project Owner comes from the initiation  -->
<!-- request of the document, if any), a row per approver or  -->
<!-- reviewer, a row per revision (latest first) and the      -->
<!-- location of the document. The HTML module shows the same -->
<!-- information as separate tables.                          -->
<!-- ======================================================== -->

<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:proteus="http://proteus.us.es"
  xmlns:proteus-utils="http://proteus.us.es/utils"
>

  <!-- A row of the card: escaped label and LaTeX content -->
  <xsl:template name="document_control_row">
    <xsl:param name="label"/>
    <xsl:param name="content"/>
    <xsl:if test="normalize-space($content) != ''">
      <xsl:call-template name="tex"><xsl:with-param name="text" select="$label"/></xsl:call-template>
      <xsl:text> &amp; </xsl:text>
      <xsl:value-of select="$content"/>
      <xsl:text> \\ \hline&#10;</xsl:text>
    </xsl:if>
  </xsl:template>

  <!-- Targets of a trace property, separated by commas -->
  <xsl:template name="document_control_targets">
    <xsl:param name="property"/>
    <xsl:for-each select="$property/trace">
      <xsl:variable name="target" select="//object[@id = current()/@target]"/>
      <xsl:if test="$target">
        <xsl:if test="position() > 1"><xsl:text>, </xsl:text></xsl:if>
        <xsl:call-template name="trace_target">
          <xsl:with-param name="target_object" select="$target"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:for-each>
  </xsl:template>

  <xsl:template
    match="object[contains(concat(' ', normalize-space(@classes), ' '),' document-control ')]"
    name="document_control_template"
    priority="1"
  >
    <xsl:variable name="document"
      select="ancestor::object[contains(concat(' ', normalize-space(@classes), ' '), ' :Proteus-document ')][1]"/>
    <xsl:variable name="request"
      select="$document//object[contains(concat(' ', normalize-space(@classes), ' '), ' initiation-request ')][1]"/>

    <xsl:variable name="rows">
      <xsl:call-template name="document_control_row">
        <xsl:with-param name="label" select="proteus-utils:i18n('xslt.document_title')"/>
        <xsl:with-param name="content">
          <xsl:call-template name="tex"><xsl:with-param name="text" select="$document/properties/*[@name=':Proteus-name']"/></xsl:call-template>
        </xsl:with-param>
      </xsl:call-template>
      <xsl:call-template name="document_control_row">
        <xsl:with-param name="label" select="proteus-utils:i18n('xslt.project_title')"/>
        <xsl:with-param name="content">
          <xsl:call-template name="tex"><xsl:with-param name="text" select="$document/parent::*/parent::*/properties/*[@name=':Proteus-name']"/></xsl:call-template>
        </xsl:with-param>
      </xsl:call-template>
      <xsl:call-template name="document_control_row">
        <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.document-author')"/>
        <xsl:with-param name="content">
          <xsl:call-template name="document_control_targets">
            <xsl:with-param name="property" select="$document/properties/traceProperty[@name='document-author']"/>
          </xsl:call-template>
        </xsl:with-param>
      </xsl:call-template>
      <xsl:call-template name="document_control_row">
        <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.project-owner')"/>
        <xsl:with-param name="content">
          <xsl:call-template name="document_control_targets">
            <xsl:with-param name="property" select="$request/properties/traceProperty[@name='project-owner']"/>
          </xsl:call-template>
        </xsl:with-param>
      </xsl:call-template>
      <xsl:call-template name="document_control_row">
        <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.project-manager')"/>
        <xsl:with-param name="content">
          <xsl:call-template name="document_control_targets">
            <xsl:with-param name="property" select="$document/properties/traceProperty[@name='project-manager']"/>
          </xsl:call-template>
        </xsl:with-param>
      </xsl:call-template>
      <xsl:call-template name="document_control_row">
        <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.version')"/>
        <xsl:with-param name="content">
          <xsl:call-template name="tex"><xsl:with-param name="text" select="$document/properties/*[@name='version']"/></xsl:call-template>
        </xsl:with-param>
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

      <!-- Approvers and reviewers: "<action>: <name> (<role>), <date>" -->
      <xsl:for-each select="children/object[contains(concat(' ', normalize-space(@classes), ' '), ' approval ')]">
        <xsl:variable name="approver"
          select="//object[@id = current()/properties/traceProperty[@name='approver']/trace[1]/@target]"/>
        <xsl:call-template name="document_control_row">
          <xsl:with-param name="label">
            <xsl:value-of select="proteus-utils:i18n(concat('archetype.enum_choices.', properties/enumProperty[@name='action']))"/>
          </xsl:with-param>
          <xsl:with-param name="content">
            <xsl:call-template name="document_control_targets">
              <xsl:with-param name="property" select="properties/traceProperty[@name='approver']"/>
            </xsl:call-template>
            <xsl:if test="normalize-space($approver/properties/*[@name='role']) != ''">
              <xsl:text>, </xsl:text>
              <xsl:call-template name="tex"><xsl:with-param name="text" select="$approver/properties/*[@name='role']"/></xsl:call-template>
            </xsl:if>
            <xsl:text> (</xsl:text>
            <xsl:value-of select="properties/*[@name=':Proteus-date']"/>
            <xsl:text>)</xsl:text>
          </xsl:with-param>
        </xsl:call-template>
      </xsl:for-each>

      <!-- History, latest revision first: "<revision> & <date>, <author>: <changes>" -->
      <xsl:for-each select="children/object[contains(concat(' ', normalize-space(@classes), ' '), ' revision ')]">
        <xsl:sort select="properties/*[@name=':Proteus-date']" order="descending"/>
        <xsl:sort select="properties/*[@name='revision']" order="descending"/>
        <xsl:call-template name="document_control_row">
          <xsl:with-param name="label"
            select="concat(proteus-utils:i18n('archetype.prop_name.revision'), ' ', properties/*[@name='revision'])"/>
          <xsl:with-param name="content">
            <xsl:value-of select="properties/*[@name=':Proteus-date']"/>
            <xsl:if test="properties/traceProperty[@name='created-by']/trace">
              <xsl:text>, </xsl:text>
              <xsl:call-template name="document_control_targets">
                <xsl:with-param name="property" select="properties/traceProperty[@name='created-by']"/>
              </xsl:call-template>
            </xsl:if>
            <xsl:if test="normalize-space(properties/*[@name='changes']) != ''">
              <xsl:text>: </xsl:text>
              <xsl:call-template name="tex"><xsl:with-param name="text" select="normalize-space(properties/*[@name='changes'])"/></xsl:call-template>
            </xsl:if>
          </xsl:with-param>
        </xsl:call-template>
      </xsl:for-each>

      <xsl:call-template name="document_control_row">
        <xsl:with-param name="label" select="proteus-utils:i18n('archetype.prop_name.document-location')"/>
        <xsl:with-param name="content">
          <xsl:call-template name="tex"><xsl:with-param name="text" select="$document/properties/*[@name='document-location']"/></xsl:call-template>
        </xsl:with-param>
      </xsl:call-template>
    </xsl:variable>

    <xsl:call-template name="generate_table">
      <xsl:with-param name="excluded_properties" select="',:Proteus-name,:Proteus-code,:Proteus-date,version,authors,sources,comments,'"/>
      <xsl:with-param name="extra_rows_before" select="string($rows)"/>
      <xsl:with-param name="show_children" select="false()"/>
    </xsl:call-template>
  </xsl:template>

</xsl:stylesheet>
