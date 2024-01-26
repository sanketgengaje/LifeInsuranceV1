import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;

import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.testng.TestNG;
import org.testng.xml.XmlClass;
import org.testng.xml.XmlSuite;
import org.testng.xml.XmlTest;

public class TestDriver {
    public static void main(String[] args) throws IOException {
        Globals.initialize();

        Workbook wbSuites = new XSSFWorkbook(new File("data\\test_suites.xlsx")); // The main test suites file
        Sheet sheetSuites = wbSuites.getSheetAt(0);
        for (Row row : sheetSuites) {
            if (row.getCell(2).getStringCellValue().equals("y")) { // checking for the suite run condition
                Workbook wbTestSuite = new XSSFWorkbook(new File(row.getCell(1).getStringCellValue())); // loading the test suite file
                Sheet sheetTestSuite = wbTestSuite.getSheetAt(0);
                for (Row moduleRow : sheetTestSuite) {
                    if (moduleRow.getCell(2).getStringCellValue().equals("y")) { // checking for the module run condition
                        Workbook wbTestFile = new XSSFWorkbook(new File(moduleRow.getCell(1).getStringCellValue())); // loading the test module file
                        Sheet sheetTestFile = wbTestFile.getSheetAt(0);
                        for (Row testRow : sheetTestFile) {
                            if (testRow.getCell(2).getStringCellValue().equals("y")) { // checking for the test run condition
                                // setting up the key as file name + test method name
                                Globals.testsToRun.put(
                                    "tests\\" + testRow.getCell(0).getStringCellValue() + "::" + testRow.getCell(1).getStringCellValue(),
                                    new String[] {testRow.getCell(1).getStringCellValue(), moduleRow.getCell(1).getStringCellValue()}); // assigning test data file to the test
                            }
                        }
                        wbTestFile.close();
                    }
                }
                wbTestSuite.close();
            }
        }
        wbSuites.close();

        SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MMM-yyyy(HH-mm-ss-a)");
        String reportFileName = "reports\\report_" + dateFormat.format(new Date()) + ".html";

        XmlSuite suite = new XmlSuite();
        suite.setName("TestSuite");
        suite.addListener("org.uncommons.reportng.HTMLReporter");
    }
}