<?xml version="1.0" encoding="utf-8"?>

<!-- ======================================================== -->
<!-- File    : alternative.xsl                                -->
<!-- Content : PM2 XSLT for the alternatives of a Business    -->
<!--           Case                                           -->
<!-- Author  : Amador Durán Toro & Claude Code                -->
<!-- Date    : 2026/10/20                                     -->
<!-- Version : 1.0                                            -->
<!-- ======================================================== -->
<!-- The SWOT analysis is shown as a 2x2 grid after the       -->
<!-- other properties, and the chosen alternative is marked   -->
<!-- in the header instead of a row.                          -->
<!-- ======================================================== -->

<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:proteus="http://proteus.us.es"
  xmlns:proteus-utils="http://proteus.us.es/utils"
  exclude-result-prefixes="proteus proteus-utils"
>

  <!-- A quadrant of the SWOT grid -->
  <xsl:template name="swot_cell">
    <xsl:param name="property"/>
    <td class="swot_{$property}">
      <div class="swot_label">
        <xsl:value-of select="proteus-utils:i18n(concat('archetype.prop_name.', $property))"/>
      </div>
      <xsl:call-template name="generate_markdown">
        <xsl:with-param name="content" select="properties/*[@name=$property]"/>
      </xsl:call-template>
    </td>
  </xsl:template>

  <xsl:template
    match="object[contains(concat(' ', normalize-space(@classes), ' '),' alternative ')]"
    name="alternative_template"
    priority="1"
  >
    <xsl:variable name="postfix">
      <xsl:if test="properties/booleanProperty[@name='chosen'] = 'true'">
        <xsl:value-of select="proteus-utils:i18n('xslt.chosen')"/>
      </xsl:if>
    </xsl:variable>

    <xsl:variable name="swot_rows">
      <xsl:if test="properties/*[@name='strengths' or @name='weaknesses' or @name='opportunities' or @name='threats'][normalize-space() != '']">
        <tr>
          <td colspan="2" class="wide_property">
            <div class="wide_property_label">
              <xsl:value-of select="proteus-utils:i18n('xslt.swot')"/>
            </div>
            <table class="swot">
              <tr>
                <xsl:call-template name="swot_cell"><xsl:with-param name="property" select="'strengths'"/></xsl:call-template>
                <xsl:call-template name="swot_cell"><xsl:with-param name="property" select="'weaknesses'"/></xsl:call-template>
              </tr>
              <tr>
                <xsl:call-template name="swot_cell"><xsl:with-param name="property" select="'opportunities'"/></xsl:call-template>
                <xsl:call-template name="swot_cell"><xsl:with-param name="property" select="'threats'"/></xsl:call-template>
              </tr>
            </table>
          </td>
        </tr>
      </xsl:if>
      <!-- The assessment, the reasons for the choice and the comments go after the SWOT grid -->
      <xsl:for-each select="properties/*[@name='assessment' or @name='selection-rationale' or @name='comments']">
        <xsl:call-template name="generate_property_row"/>
      </xsl:for-each>
    </xsl:variable>

    <xsl:call-template name="generate_table">
      <xsl:with-param name="postfix" select="string($postfix)"/>
      <xsl:with-param name="excluded_properties"
        select="',:Proteus-name,:Proteus-code,:Proteus-date,version,authors,sources,strengths,weaknesses,opportunities,threats,chosen,assessment,selection-rationale,comments,'"/>
      <xsl:with-param name="extra_rows" select="$swot_rows"/>
    </xsl:call-template>
  </xsl:template>

</xsl:stylesheet>
