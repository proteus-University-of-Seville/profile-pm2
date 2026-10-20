<?xml version="1.0" encoding="utf-8"?>

<!-- ======================================================== -->
<!-- File    : cost_plan.xsl                                  -->
<!-- Content : PM2 XSLT for the cost plan of a Business Case  -->
<!--           or a Project Charter                           -->
<!-- Author  : Amador Durán Toro & Claude Code                -->
<!-- Date    : 2026/10/20                                     -->
<!-- Version : 1.1                                            -->
<!-- ======================================================== -->
<!-- Renders the Total Cost of Ownership tables of PM2: one   -->
<!-- table per group of costs (solution implementation,       -->
<!-- business implementation), one row per cost with its      -->
<!-- budget line (if any cost of the group has one), one      -->
<!-- column per year and the total, and the totals of staff   -->
<!-- (FTE) and of other costs (k€).                           -->
<!-- ======================================================== -->
<!-- Update  : 2026/10/20 (Amador Durán & Claude Code)        -->
<!-- Budget lines, total column and previous investments, for -->
<!-- the Project Charter.                                     -->
<!-- ======================================================== -->

<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:proteus="http://proteus.us.es"
  xmlns:proteus-utils="http://proteus.us.es/utils"
  exclude-result-prefixes="proteus proteus-utils"
>

  <!-- Value of a cost, without trailing zeros -->
  <xsl:template name="cost_value">
    <xsl:param name="value"/>
    <xsl:value-of select="format-number($value, '0.##')"/>
  </xsl:template>

  <!-- Row of totals of the costs of one nature, if there is any -->
  <xsl:template name="cost_total_row">
    <xsl:param name="items"/>
    <xsl:param name="label_key"/>
    <xsl:param name="budget_lines"/>
    <xsl:if test="$items">
      <tr class="cost_total">
        <th><xsl:value-of select="proteus-utils:i18n($label_key)"/></th>
        <xsl:if test="$budget_lines"><td class="budget_line"/></xsl:if>
        <xsl:for-each select="$items[1]/properties/floatProperty[starts-with(@name, 'year-')]">
          <xsl:variable name="year" select="@name"/>
          <td>
            <xsl:call-template name="cost_value">
              <xsl:with-param name="value" select="sum($items/properties/floatProperty[@name=$year])"/>
            </xsl:call-template>
          </td>
        </xsl:for-each>
        <td class="cost_row_total">
          <xsl:call-template name="cost_value">
            <xsl:with-param name="value" select="sum($items/properties/floatProperty[starts-with(@name, 'year-')])"/>
          </xsl:call-template>
        </td>
      </tr>
    </xsl:if>
  </xsl:template>

  <!-- Table of a group of costs -->
  <xsl:template name="cost_table">
    <xsl:param name="group"/>
    <xsl:param name="first_year"/>
    <xsl:variable name="items"
      select="children/object[contains(concat(' ', normalize-space(@classes), ' '), ' cost-item ')][properties/enumProperty[@name='group'] = $group]"/>
    <xsl:variable name="budget_lines"
      select="boolean($items/properties/*[@name='budget-line'][normalize-space() != ''])"/>

    <xsl:if test="$items">
      <tr>
        <td colspan="2" class="wide_property">
          <table class="cost_table">
            <caption><xsl:value-of select="proteus-utils:i18n(concat('archetype.enum_choices.', $group))"/></caption>
            <thead>
              <tr>
                <th><xsl:value-of select="proteus-utils:i18n('xslt.cost_concept')"/></th>
                <xsl:if test="$budget_lines">
                  <th><xsl:value-of select="proteus-utils:i18n('archetype.prop_name.budget-line')"/></th>
                </xsl:if>
                <xsl:for-each select="$items[1]/properties/floatProperty[starts-with(@name, 'year-')]">
                  <th>
                    <xsl:choose>
                      <xsl:when test="$first_year > 0">
                        <xsl:value-of select="$first_year + position() - 1"/>
                      </xsl:when>
                      <xsl:otherwise>
                        <xsl:value-of select="proteus-utils:i18n(concat('archetype.prop_name.', @name))"/>
                      </xsl:otherwise>
                    </xsl:choose>
                  </th>
                </xsl:for-each>
                <th><xsl:value-of select="proteus-utils:i18n('xslt.cost_total')"/></th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="$items">
                <tr id="{@id}" data-proteus-id="{@id}">
                  <th>
                    <xsl:value-of select="properties/*[@name=':Proteus-name']"/>
                    <span class="cost_unit">
                      <xsl:choose>
                        <xsl:when test="properties/enumProperty[@name='nature'] = 'staff'">
                          <xsl:value-of select="proteus-utils:i18n('xslt.unit_fte')"/>
                        </xsl:when>
                        <xsl:otherwise>
                          <xsl:value-of select="proteus-utils:i18n('xslt.unit_keur')"/>
                        </xsl:otherwise>
                      </xsl:choose>
                    </span>
                  </th>
                  <xsl:if test="$budget_lines">
                    <td class="budget_line"><xsl:value-of select="properties/*[@name='budget-line']"/></td>
                  </xsl:if>
                  <xsl:for-each select="properties/floatProperty[starts-with(@name, 'year-')]">
                    <td>
                      <xsl:call-template name="cost_value">
                        <xsl:with-param name="value" select="."/>
                      </xsl:call-template>
                    </td>
                  </xsl:for-each>
                  <td class="cost_row_total">
                    <xsl:call-template name="cost_value">
                      <xsl:with-param name="value" select="sum(properties/floatProperty[starts-with(@name, 'year-')])"/>
                    </xsl:call-template>
                  </td>
                </tr>
              </xsl:for-each>
              <xsl:call-template name="cost_total_row">
                <xsl:with-param name="items" select="$items[properties/enumProperty[@name='nature'] = 'staff']"/>
                <xsl:with-param name="label_key" select="'xslt.total_staff'"/>
                <xsl:with-param name="budget_lines" select="$budget_lines"/>
              </xsl:call-template>
              <xsl:call-template name="cost_total_row">
                <xsl:with-param name="items" select="$items[properties/enumProperty[@name='nature'] != 'staff']"/>
                <xsl:with-param name="label_key" select="'xslt.total_other'"/>
                <xsl:with-param name="budget_lines" select="$budget_lines"/>
              </xsl:call-template>
            </tbody>
          </table>
        </td>
      </tr>
    </xsl:if>
  </xsl:template>

  <!-- ================================================================== -->
  <!-- cost-plan template                                                 -->
  <!-- ================================================================== -->

  <xsl:template
    match="object[contains(concat(' ', normalize-space(@classes), ' '),' cost-plan ')]"
    name="cost_plan_template"
    priority="1"
  >
    <xsl:variable name="first_year" select="number(properties/*[@name='first-year'])"/>

    <xsl:variable name="cost_rows">
      <xsl:call-template name="cost_table">
        <xsl:with-param name="group" select="'solution-implementation'"/>
        <xsl:with-param name="first_year" select="$first_year"/>
      </xsl:call-template>
      <xsl:call-template name="cost_table">
        <xsl:with-param name="group" select="'business-implementation'"/>
        <xsl:with-param name="first_year" select="$first_year"/>
      </xsl:call-template>
      <xsl:for-each select="properties/*[@name='funding-source' or @name='previous-investments' or @name='comments']">
        <xsl:call-template name="generate_property_row"/>
      </xsl:for-each>
    </xsl:variable>

    <xsl:call-template name="generate_table">
      <xsl:with-param name="excluded_properties"
        select="',:Proteus-name,:Proteus-code,:Proteus-date,version,authors,sources,first-year,funding-source,previous-investments,comments,'"/>
      <xsl:with-param name="extra_rows" select="$cost_rows"/>
      <xsl:with-param name="show_children" select="false()"/>
    </xsl:call-template>
  </xsl:template>

</xsl:stylesheet>
