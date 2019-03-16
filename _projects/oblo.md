---
layout: project
title: 'IoT Home Automation'
date: 1 Mar 2017
image: /assets/img/projects/iotsmarthome.png
screenshot: /assets/img/projects/iotsmarthome.png
links:
  - title: Website
    url: http://www.obloliving.com/
  - title: Demo
    url: https://itunes.apple.com/us/app/oblo-living/id1041414923?mt=8
caption: Smart Home - IoT
description: >
  Milovan Tomašević worked as an iOS developer at the OBLO Living within the project "Smart Home - IoT ...
hide_description: true
accent_image: /assets/img//projects/smarthome.jpg
accent_color: rgb(65,105,225)

---


OBLO Living provides world-class solutions for home automation (HA). We combine our end-to-end software solution for HA with in-house developed HA devices to cover lighting, security, safety, energy management and other aspects of the fast-growing home automation markets.

- iOS application development
- Programming in Objective C language
- Working with xCode software
- Working with Cocoa Touch frameworks (Foundation, UIKit, CoreData, iOS SDK, Foscam SDK etc.)
- Designing & Development of Appium test automation scripts for iOS & Android Mobile applications.
- Selenium-WebDriver JS with Automation Framework built-TypeScript See less

![](/assets/img/projects/job.JPG)
Work time
{:.figure}

~~~swift
-(void)loginButtonClicked:(UIButton*)sender
{
    LogI(@"Login button clicked");

    userName = _emailLoginField.text;
    password = _passwordLoginField.text;
    userName = [userName stringByTrimmingCharactersInSet: [NSCharacterSet whitespaceCharacterSet]];
    password = [password stringByTrimmingCharactersInSet: [NSCharacterSet whitespaceCharacterSet]];

    if ([userName isEqualToString:@""]) {
        [ALERT_PRESENTER presentAlertWithTitle:NSLocalizedString(@"error",nil) message:NSLocalizedString(@"msg_1a",nil)];
        return;
    }
    if ([password isEqualToString:@""]) {
        [ALERT_PRESENTER presentAlertWithTitle:NSLocalizedString(@"error",nil) message:NSLocalizedString(@"msg_2",nil)];
        return;
    }

    CoreDataManager *coreDataManager = [[CoreDataManager alloc]init];
    User *user = [coreDataManager loginUser:userName password:password];
    
    if(([userName isEqualToString:@"Admin"] && [password isEqualToString:@"Admin"]) || user != nil ){
        MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.navigationController.view animated:YES];
        hud.mode = MBProgressHUDModeCustomView;
        UIImage *image = [[UIImage imageNamed:@"Checkmark"] imageWithRenderingMode:UIImageRenderingModeAlwaysTemplate];
        hud.customView = [[UIImageView alloc] initWithImage:image];
        hud.square = YES;
        hud.label.text = [NSString stringWithFormat:NSLocalizedString(@"welcome", nil), userName ];
        [hud hideAnimated:YES afterDelay:1.f];
        
        //store data
        [[NSUserDefaults standardUserDefaults] setValue:userName forKey:PREF_USER_EMAIL];
        [[NSUserDefaults standardUserDefaults] setValue:password forKey:PREF_USER_PASSWORD];
        [[NSUserDefaults standardUserDefaults] setBool:YES forKey:PREF_USER_LOGIN];
        [[NSUserDefaults standardUserDefaults] synchronize];
        
        [self.navigationController popToRootViewControllerAnimated:YES];
    
    }else{
        [ALERT_PRESENTER presentAlertWithTitle:NSLocalizedString(@"error",nil) message:NSLocalizedString(@"msg_19",nil)];
    }
}
~~~
objC Examples Login
{:.figure}

~~~swift
- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear: animated];

    [_menuQuality dismissViewControllerAnimated:NO completion:nil];
    [_cameraRecognizer addGestureRecognizer:imageV];
    [self displayHeaderAndFooter];
    
    reOpenVideo = NO;
    
    LogI(@"Usao u didAppear");

        [_menuQuality dismissViewControllerAnimated:NO completion:nil];
        [_cameraRecognizer addGestureRecognizer:imageV];
        [self displayHeaderAndFooter];
        
        reOpenVideo = NO;
        
        LogI(@"Usao u didAppear");
        
        int right = 0;
        FOSCMD_RESULT rst = FosSdk_Login(mHandle, &right, 300);
    
    if (rst == FOSCMDRET_TIMEOUT){
        //[ALERT_PRESENTER presentAlertWithTitle:@"FOSCMDRET_TIMEOUT" message:@"TRY_AGAIN"];

        rst = FosSdk_Login(mHandle, &right, 300);
        if (rst == FOSUSRRET_USRNAMEORPWD_ERR){
            
            [self reLogin];
            return;
        }
        [self CloseAllOperation];
        [self startAll];
    
    }
    
        if (rst == FOSUSRRET_USRNAMEORPWD_ERR){
            
            [self reLogin];
            return;
        }
        
        if([_sesija.sPass isEqualToString:@""]){ 
            Camera *changeFirstData = [coreDataManager getCameraWithUid:self.sesija.sUID];
            if([changeFirstData.password isEqualToString:@""]){
                NewCamDataViewController *ncdvc = [[NewCamDataViewController alloc]init];
                ncdvc.delegate = self;
                [ncdvc setTitle:[NSString stringWithFormat:NSLocalizedString(@"new_data",nil)]];
                ncdvc.newHandle = mHandle;
                [self.navigationController presentViewController:ncdvc animated:YES completion:nil];
            }
            _sesija.sPass = changeFirstData.password;
        }

        if (rst == FOSCMDRET_OK){
            
            [self startAll];
        }else if (rst == FOSCMDRET_TIMEOUT){
            [ALERT_PRESENTER presentAlertWithTitle:@"FOSCMDRET_TIMEOUT" message:@"TRY_AGAIN"];
            [self CloseAllOperation];
            [self startAll];
        }else{
            [self messagePresent];
        }
}
~~~
objC Examples Open video
{:.figure}

<figure>
  <video src="/assets/img/projects/oblo.mp4" class="border" controls muted autoplay loop><img data-ignore alt="Cover page slide animation" src="/assets/img/blog/cover-page.png"/></video>
  <figcaption>Testing code</figcaption>
</figure>


~~~java
package iOS;

import Utils.Config;
import Utils.Config.iOS;
import io.appium.java_client.ios.IOSDriver;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Login {
    IOSDriver driver;

    public Login() {
    }

    @Before
    public void setup() throws MalformedURLException, InterruptedException {
        this.driver = new IOSDriver(new URL("http://0.0.0.0:4723/wd/hub"), iOS.getCapabilities());
        this.driver.manage().timeouts().implicitlyWait(60L, TimeUnit.SECONDS);
        this.driver.findElement(By.name("Allow")).click();
        Thread.sleep(1000L);
    }

    @After
    public void teardown() {
        this.driver.quit();
    }

    @Test
    public void LOGIN_withoutMail() throws InterruptedException {
        System.out.println("Start LOGIN_withoutMail " + Config.getTimeStamp());
        this.driver.findElement(By.xpath("//XCUIElementTypeTextField")).sendKeys(new CharSequence[]{""});
        this.driver.findElement(By.xpath("//XCUIElementTypeSecureTextField")).sendKeys(new CharSequence[]{"Test"});
        this.driver.findElement(By.name("Next")).click();
        WebDriverWait wait = new WebDriverWait(this.driver, 2L);
        wait.until(ExpectedConditions.alertIsPresent());
        Alert alert = this.driver.switchTo().alert();
        Assert.assertTrue(alert.getText().contains("You need to enter user email first."));
        alert.accept();
        System.out.println("Finish LOGIN_withoutMail " + Config.getTimeStamp());
    }

    @Test
    public void LOGIN_withoutPassword() throws InterruptedException {
        System.out.println("Start LOGIN_withoutPassword " + Config.getTimeStamp());
        this.driver.findElement(By.xpath("//XCUIElementTypeTextField")).sendKeys(new CharSequence[]{"milovan.tomasevic@rt-rk.com"});
        this.driver.findElement(By.xpath("//XCUIElementTypeSecureTextField")).sendKeys(new CharSequence[]{""});
        this.driver.findElement(By.name("Next")).click();
        WebDriverWait wait = new WebDriverWait(this.driver, 2L);
        wait.until(ExpectedConditions.alertIsPresent());
        Alert alert = this.driver.switchTo().alert();
        Assert.assertTrue(alert.getText().contains("You need to enter password first."));
        alert.accept();
        System.out.println("Finish LOGIN_withoutPassword " + Config.getTimeStamp());
    }

    @Test
    public void LOGIN_incorrectData() throws InterruptedException {
        System.out.println("Start LOGIN_incorrectData " + Config.getTimeStamp());
        this.driver.findElement(By.xpath("//XCUIElementTypeTextField")).sendKeys(new CharSequence[]{"Test"});
        this.driver.findElement(By.xpath("//XCUIElementTypeSecureTextField")).sendKeys(new CharSequence[]{"Test"});
        this.driver.findElement(By.name("Next")).click();
        WebDriverWait wait = new WebDriverWait(this.driver, 2L);
        wait.until(ExpectedConditions.alertIsPresent());
        Alert alert = this.driver.switchTo().alert();
        Assert.assertTrue(alert.getText().contains("Incorrect user name or password."));
        alert.accept();
        System.out.println("Finish LOGIN_incorrectData " + Config.getTimeStamp());
    }

    @Test
    public void LOGIN_correct() throws InterruptedException {
        System.out.println("Start LOGIN_correct  " + Config.getTimeStamp());
        this.driver.findElement(By.xpath("//XCUIElementTypeTextField")).sendKeys(new CharSequence[]{"milovan.tomasevic@rt-rk.com"});
        this.driver.findElement(By.xpath("//XCUIElementTypeSecureTextField")).sendKeys(new CharSequence[]{"Test1234"});
        this.driver.findElement(By.name("Next")).click();
        Thread.sleep(1000L);
        this.driver.findElement(By.name("reveal icon")).click();
        Thread.sleep(1000L);
        System.out.println("Finish LOGIN_correct " + Config.getTimeStamp());
    }
}

~~~
Test for Login (Java)
{:.figure}

![](/assets/img/projects/game.JPG)
It pays to play — and laugh and party and have fun — at work, and that's no joke
{:.figure}

![](/assets/img/projects/pause.JPG)
Happy work team during break time
{:.figure}

![](/assets/img/projects/game2.JPG)
It pays to play — and laugh and party and have fun — at work, and that's no joke
{:.figure}