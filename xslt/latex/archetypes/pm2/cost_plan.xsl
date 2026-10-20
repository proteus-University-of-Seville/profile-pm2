<?xml version="1.0" encoding="utf-8"?>

<!-- ======================================================== -->
<!-- File    : cost_plan.xsl                                  -->
<!-- Content : PM2 LaTeX XSLT for the cost plan of a Business -->
<!--           Case or a Project Charter                      -->
<!-- Author  : Amador Durán Toro & Claude Code                -->
<!-- Date    : 2026/10/20                                     -->
<!-- Version : 1.1                                            -->
<!-- ======================================================== -->
<!-- The card shows the funding source and the previous       -->
<!-- investments; below it, a Total Cost of Ownership table   -->
<!-- per group of costs, with a row per cost (and its budget  -->
<!-- line, if any cost of the group has one), a column per    -->
<!-- year and the total, and the totals of staff (FTE) and of -->
<!-- other costs (k€).                                        -->
<!-- ======================================================== -->

<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:proteus="http://proteus.us.es"
  xmlns:proteus-utils="http://proteus.us.es/utils"
>

  <xsl:template name="latex_cost_total_row">
    <xsl:param name="items"/>
    <xsl:param name="label_key"/>
    <xsl:param name="budget_lines"/>
    <xsl:if test="$items">
      <xsl:text>\textbf{</xsl:text>
      <xsl:call-template name="label"><xsl:with-param name="key" select="$label_key"/></xsl:call-template>
      <xsl:text>}</xsl:text>
      <xsl:if test="$budget_lines"><xsl:text> &amp; </xsl:text></xsl:if>
      <xsl:for-each select="$items[1]/properties/floatProperty[starts-with(@name, 'year-')]">
        <xsl:variable name="year" select="@name"/>
        <xsl:text> &amp; \textbf{</xsl:text>
        <xsl:value-of select="format-number(sum($items/properties/floatProperty[@name=$year]), '0.##')"/>
        <xsl:text>}</xsl:text>
      </xsl:for-each>
      <xsl:text> &amp; \textbf{</xsl:text>
      <xsl:value-of select="format-number(sum($items/properties/floatProperty[starts-with(@name, 'year-')]), '0.##')"/>
      <xsl:text>} \\ \hline&#10;</xsl:text>
    </xsl:if>
  </xsl:template>

  <xsl:template name="latex_cost_table">
    <xsl:param name="group"/>
    <xsl:param name="first_year"/>
    <xsl:variable name="items"
      select="children/object[contains(concat(' ', normalize-space(@classes), ' '), ' cost-item ')][properties/enumProperty[@name='group'] = $group]"/>
    <xsl:variable name="budget_lines"
      select="boolean($items/properties/*[@name='budget-line'][normalize-space() != ''])"/>
    <xsl:variable name="years" select="count($items[1]/properties/floatProperty[starts-with(@name, 'year-')])"/>
    <xsl:variable name="columns" select="$years + 2 + number($budget_lines)"/>

    <xsl:if test="$items">
      <xsl:text>\begin{center}\small&#10;\begin{tabular}{|</xsl:text>
      <xsl:choose>
        <xsl:when test="$budget_lines">&gt;{\raggedright\arraybackslash}p{0.27\linewidth}|&gt;{\raggedright\arraybackslash}p{0.13\linewidth}|</xsl:when>
        <xsl:otherwise>&gt;{\raggedright\arraybackslash}p{0.36\linewidth}|</xsl:otherwise>
      </xsl:choose>
      <xsl:for-each select="$items[1]/properties/floatProperty[starts-with(@name, 'year-')]">r|</xsl:for-each>
      <xsl:text>r|}\hline&#10;</xsl:text>
      <xsl:text>\multicolumn{</xsl:text>
      <xsl:value-of select="$columns"/>
      <xsl:text>}{|l|}{\textbf{</xsl:text>
      <xsl:call-template name="label"><xsl:with-param name="key" select="concat('archetype.enum_choices.', $group)"/></xsl:call-template>
      <xsl:text>}} \\ \hline&#10;\textbf{</xsl:text>
      <xsl:call-template name="label"><xsl:with-param name="key" select="'xslt.cost_concept'"/></xsl:call-template>
      <xsl:text>}</xsl:text>
      <xsl:if test="$budget_lines">
        <xsl:text> &amp; \textbf{</xsl:text>
        <xsl:call-template name="label"><xsl:with-param name="key" select="'archetype.prop_name.budget-line'"/></xsl:call-template>
        <xsl:text>}</xsl:text>
      </xsl:if>
      <xsl:for-each select="$items[1]/properties/floatProperty[starts-with(@name, 'year-')]">
        <xsl:text> &amp; \textbf{</xsl:text>
        <xsl:choose>
          <xsl:when test="$first_year > 0"><xsl:value-of select="$first_year + position() - 1"/></xsl:when>
          <xsl:otherwise>
            <xsl:call-template name="label"><xsl:with-param name="key" select="concat('archetype.prop_name.', @name)"/></xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
        <xsl:text>}</xsl:text>
      </xsl:for-each>
      <xsl:text> &amp; \textbf{</xsl:text>
      <xsl:call-template name="label"><xsl:with-param name="key" select="'xslt.cost_total'"/></xsl:call-template>
      <xsl:text>} \\ \hline&#10;</xsl:text>

      <xsl:for-each select="$items">
        <xsl:call-template name="tex"><xsl:with-param name="text" select="properties/*[@name=':Proteus-name']"/></xsl:call-template>
        <xsl:choose>
          <xsl:when test="properties/enumProperty[@name='nature'] = 'staff'">
            <xsl:call-template name="label"><xsl:with-param name="key" select="'xslt.unit_fte'"/></xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <xsl:call-template name="label"><xsl:with-param name="key" select="'xslt.unit_keur'"/></xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
        <xsl:if test="$budget_lines">
          <xsl:text> &amp; </xsl:text>
          <xsl:call-template name="tex"><xsl:with-param name="text" select="properties/*[@name='budget-line']"/></xsl:call-template>
        </xsl:if>
        <xsl:for-each select="properties/floatProperty[starts-with(@name, 'year-')]">
          <xsl:text> &amp; </xsl:text>
          <xsl:value-of select="format-number(., '0.##')"/>
        </xsl:for-each>
        <xsl:text> &amp; </xsl:text>
        <xsl:value-of select="format-number(sum(properties/floatProperty[starts-with(@name, 'year-')]), '0.##')"/>
        <xsl:text> \\ \hline&#10;</xsl:text>
      </xsl:for-each>

      <xsl:call-template name="latex_cost_total_row">
        <xsl:with-param name="items" select="$items[properties/enumProperty[@name='nature'] = 'staff']"/>
        <xsl:with-param name="label_key" select="'xslt.total_staff'"/>
        <xsl:with-param name="budget_lines" select="$budget_lines"/>
      </xsl:call-template>
      <xsl:call-template name="latex_cost_total_row">
        <xsl:with-param name="items" select="$items[properties/enumProperty[@name='nature'] != 'staff']"/>
        <xsl:with-param name="label_key" select="'xslt.total_other'"/>
        <xsl:with-param name="budget_lines" select="$budget_lines"/>
      </xsl:call-template>
      <xsl:text>\end{tabular}&#10;\end{center}&#10;</xsl:text>
    </xsl:if>
  </xsl:template>

  <xsl:template
    match="object[contains(concat(' ', normalize-space(@classes), ' '),' cost-plan ')]"
    name="cost_plan_template"
    priority="1"
  >
    <xsl:variable name="first_year" select="number(properties/*[@name='first-year'])"/>

    <xsl:call-template name="generate_table">
      <xsl:with-param name="excluded_properties"
        select="',:Proteus-name,:Proteus-code,:Proteus-date,version,authors,sources,first-year,'"/>
      <xsl:with-param name="show_children" select="false()"/>
    </xsl:call-template>

    <xsl:call-template name="latex_cost_table">
      <xsl:with-param name="group" select="'solution-implementation'"/>
      <xsl:with-param name="first_year" select="$first_year"/>
    </xsl:call-template>
    <xsl:call-template name="latex_cost_table">
      <xsl:with-param name="group" select="'business-implementation'"/>
      <xsl:with-param name="first_year" select="$first_year"/>
    </xsl:call-template>
  </xsl:template>

</xsl:stylesheet>
